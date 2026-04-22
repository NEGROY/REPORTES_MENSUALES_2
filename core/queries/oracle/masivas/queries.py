from collections.abc import Iterable

from core.queries.oracle.base import BaseOracleQuery


# **********************************************
class MasivasTiempoQuery(BaseOracleQuery):
    SQL = """
        WITH
            TK AS (
                SELECT
                    ps1."NUMBER" TK,
                    (SYSDATE - OPEN_TIME) T_VIDE_TK,
                    OPEN_TIME,
                    ROUND((SYSDATE - OPEN_TIME) * 24, 3) AS TOTAL_HORAS,
                    EXTRACT(DAY FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' d ' ||
                    EXTRACT(HOUR FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' h ' ||
                    EXTRACT(MINUTE FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' m' AS TIEMPO_VIDA_TK,
                    FLOOR((SYSDATE - OPEN_TIME) * 24 * 60) AS TOTAL_MINUTOS,
                    TG_ENLACE,
                    problem_type
                FROM probsummarym1 ps1
                INNER JOIN probsummarym2 ps2
                    ON ps2."NUMBER" = ps1."NUMBER"
                WHERE
                    (TG_ENLACE LIKE '%MASIV%' OR TG_ENLACE LIKE '%REGIONAL%')
                    AND CLOSE_TIME IS NULL
            )
        SELECT * FROM TK
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {}
    

# **********************************************
class FallasMasivasQuery(BaseOracleQuery):
    SQL_TEMPLATE = """
        WITH TK AS (
            SELECT
                probsummarym1."NUMBER" INCIDENTE,
                probsummarym1.company "CLIENTE",
                probsummarym2.tg_enlace "ENLACE",
                probsummarym1."OPEN_TIME" "FECHA DE APERTURA",
                probsummarym1."CLOSE_TIME" "FECHA DE CIERRE",
                CASE
                    WHEN Regexp_substr(TG_ENLACE, '(_GT_)', 1, 1, 'i') = '_GT_'
                        OR TG_ENLACE LIKE '%T'
                        OR TG_ENLACE LIKE '%GUATEMALA%' THEN 'GT'
                    WHEN Regexp_substr(TG_ENLACE, '(_SV_)', 1, 1, 'i') = '_SV_'
                        OR TG_ENLACE LIKE '%SV'
                        OR TG_ENLACE LIKE '%SALVADOR%' THEN 'SV'
                    WHEN Regexp_substr(TG_ENLACE, '(_CR_)', 1, 1, 'i') = '_CR_'
                        OR TG_ENLACE LIKE '%OC'
                        OR TG_ENLACE LIKE '%COSTA RICA%' THEN 'CR'
                    WHEN Regexp_substr(TG_ENLACE, '(_NI_)', 1, 1, 'i') = '_NI_'
                        OR TG_ENLACE LIKE '%ON'
                        OR TG_ENLACE LIKE '%NICARAGUA%' THEN 'NI'
                    WHEN Regexp_substr(TG_ENLACE, '(_HN_)', 1, 1, 'i') = '_HN_'
                        OR TG_ENLACE LIKE '%OH'
                        OR TG_ENLACE LIKE '%HONDURAS%' THEN 'HN'
                    WHEN Regexp_substr(TG_ENLACE, '(_PA_)', 1, 1, 'i') = '_PA_'
                        OR TG_ENLACE LIKE '%PA'
                        OR TG_ENLACE LIKE '%PANAMA%' THEN 'PA'
                END PAIS
            FROM probsummarym1
            INNER JOIN probsummarym2
                ON probsummarym2."NUMBER" = probsummarym1."NUMBER"
            WHERE probsummarym1.assignment IN (
                'CNOC',
                'CNOC_CBO_PROACTIVO',
                'CNOC_CBO_REACTIVO',
                'CNOC_MASIVO',
                'GESTION DE DATOS N1',
                'GESTION N1_CBO',
                'GT - ACC. EMPRESARIAL - NOC',
                'SOPORTE_N1_XT',
                'SOPORTE_N2_XT'
            )
        ),
        TK_RELACIONADO_MASIVA AS (
            SELECT
                SCRELATIONM1.DEPEND "MASIVA",
                SCRELATIONM1."SOURCE" "INCIDENTE"
            FROM SCRELATIONM1
            WHERE SOURCE_FILENAME = 'problem'
              AND DEPEND IN ({fallas_formateadas})
        )
        SELECT
            TK_RELACIONADO_MASIVA."INCIDENTE",
            TK_RELACIONADO_MASIVA."MASIVA",
            TK."FECHA DE APERTURA",
            TK."FECHA DE CIERRE",
            TK.CLIENTE,
            TK.ENLACE,
            TK.PAIS
        FROM TK
        INNER JOIN TK_RELACIONADO_MASIVA
            ON TK_RELACIONADO_MASIVA."INCIDENTE" = TK."INCIDENTE"
    """

    def get_sql(self) -> str:
        fallas_formateadas = self._formatear_fallas_sql(self.params.get('fallas', ''))
        return self.SQL_TEMPLATE.format(fallas_formateadas=fallas_formateadas)

    def get_params(self) -> dict:
        return {}

    def _formatear_fallas_sql(self, fallas: str | Iterable[str]) -> str:
        if isinstance(fallas, str):
            valores = [valor.strip().strip("'").strip('"') for valor in fallas.split(',')]
        else:
            valores = [str(valor).strip() for valor in fallas]

        valores_limpios = [valor for valor in valores if valor]

        if not valores_limpios:
            raise ValueError('Debe enviar al menos una falla masiva.')

        return ', '.join("'" + valor.replace("'", "''") + "'" for valor in valores_limpios)

#######################################################################################################################
#                                             INICIO RELOJES TICKETS                                                  #  
#######################################################################################################################
# **********************************************
class ClocksFallaQuery(BaseOracleQuery):
    SQL = """
        SELECT
            A.NAME,
            HORAS,
            EXTRACT(DAY FROM x) || ' ' ||
            LPAD(EXTRACT(HOUR FROM x), 2, '0') || ':' ||
            LPAD(EXTRACT(MINUTE FROM x), 2, '0') || ':' ||
            LPAD(EXTRACT(SECOND FROM x), 2, '0') AS TIEMPO
        FROM (
            SELECT
                KEY_CHAR,
                NAME,
                TOTAL,
                NUMTODSINTERVAL(
                    (
                        TO_DATE(TO_CHAR(total, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                        - TO_DATE('01/01/4000 00:00:00', 'DD/MM/YYYY HH24:MI:SS')
                    ) * 24 / 24,
                    'DAY'
                ) AS x,
                ROUND(
                    (
                        TO_DATE(TO_CHAR(total, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                        - TO_DATE('01/01/4000 00:00:00', 'DD/MM/YYYY HH24:MI:SS')
                    ) * 24,
                    3
                ) HORAS
            FROM CLOCKSM1
            WHERE KEY_CHAR = :FALLA
              AND TYPE = 'problem'
            ORDER BY NAME ASC
        ) A
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {
            'FALLA': self._normalize_ticket(self.params.get('falla', ''))
        }

    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()

        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket

# **********************************************
class MasivasListQuery(BaseOracleQuery):
    SQL = """
        WITH LISTADO_TK AS (
            SELECT
                SCRELATIONM1.SOURCE,
                SCRELATIONM1.SOURCE_FILENAME,
                SCRELATIONM1.DEPEND TK,
                SCRELATIONM1.SYSMODUSER,
                SCRELATIONM1.SYSMODTIME
            FROM SCRELATIONM1
            WHERE SCRELATIONM1.SOURCE = :FALLA
              AND SCRELATIONM1.DEPEND_FILENAME = 'problem'
        ),
        TK AS (
            SELECT
                PROBSUMMARYM1."NUMBER",
                TG_ENLACE,
                company,
                CLOSE_TIME,
                OPEN_TIME,
                brief_description TITULO,
                CASE
                    WHEN Regexp_substr(TG_ENLACE, '(_GT_)', 1, 1, 'i') = '_GT_'
                      OR TG_ENLACE LIKE '%T'
                      OR TG_ENLACE LIKE '%GUATEMALA%' THEN 'GT'
                    WHEN Regexp_substr(TG_ENLACE, '(_SV_)', 1, 1, 'i') = '_SV_'
                      OR TG_ENLACE LIKE '%SV'
                      OR TG_ENLACE LIKE '%SALVADOR%' THEN 'SV'
                    WHEN Regexp_substr(TG_ENLACE, '(_CR_)', 1, 1, 'i') = '_CR_'
                      OR TG_ENLACE LIKE '%OC'
                      OR TG_ENLACE LIKE '%COSTA RICA%' THEN 'CR'
                    WHEN Regexp_substr(TG_ENLACE, '(_NI_)', 1, 1, 'i') = '_NI_'
                      OR TG_ENLACE LIKE '%ON'
                      OR TG_ENLACE LIKE '%NICARAGUA%' THEN 'NI'
                    WHEN Regexp_substr(TG_ENLACE, '(_HN_)', 1, 1, 'i') = '_HN_'
                      OR TG_ENLACE LIKE '%OH'
                      OR TG_ENLACE LIKE '%HONDURAS%' THEN 'HN'
                    WHEN Regexp_substr(TG_ENLACE, '(_PA_)', 1, 1, 'i') = '_PA_'
                      OR TG_ENLACE LIKE '%PA'
                      OR TG_ENLACE LIKE '%PANAMA%' THEN 'PA'
                    ELSE 'SIN PAIS'
                END PAIS,
                :FALLA FALLA_MASIVA
            FROM PROBSUMMARYM1
            INNER JOIN PROBSUMMARYM2
                ON PROBSUMMARYM2."NUMBER" = PROBSUMMARYM1."NUMBER"
            WHERE PROBSUMMARYM1."NUMBER" IN (SELECT TK FROM LISTADO_TK)
        )
        SELECT * FROM TK
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {
            'FALLA': self._normalize_ticket(self.params.get('id', ''))
        }

    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()

        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket

 
# **********************************************
class MasivaDetalleQuery(BaseOracleQuery):
    SQL = """
        WITH
            LISTADO_TK AS (
                SELECT
                    PROBSUMMARYM1."NUMBER" TK,
                    PROBSUMMARYM1.brief_description TITULO,
                    TG_ENLACE,
                    PROBSUMMARYM1.PROBLEM_STATUS,
                    PROBSUMMARYM1.UPDATED_BY ULTIMA_ACTUALIZACION,
                    ASSIGN_DEPT,
                    PROBSUMMARYM1.SYSMODTIME,
                    ROUND((SYSDATE - SYSMODTIME) * 24, 2) TIEMPO_SIN_SEGUIMIENTO_HORAS,
                    TO_CHAR(TRUNC((SYSDATE - SYSMODTIME) * 24)) || ':' ||
                    LPAD(TRUNC(MOD((SYSDATE - SYSMODTIME) * 24 * 60, 60)), 2, '0') || ':' ||
                    LPAD(TRUNC(MOD((SYSDATE - SYSMODTIME) * 24 * 60 * 60, 60)), 2, '0') TIEMPO_SIN_SEGUIMIENTO_F,
                    assignment,
                    opened_by,
                    OPEN_TIME,
                    ROUND((SYSDATE - OPEN_TIME) * 24, 3) AS TOTAL_HORAS,
                    EXTRACT(DAY FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' d ' ||
                    EXTRACT(HOUR FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' h ' ||
                    EXTRACT(MINUTE FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' m' AS TIEMPO_VIDA_TK,
                    FLOOR((SYSDATE - OPEN_TIME) * 24 * 60) AS TOTAL_MINUTOS,
                    NVL(
                        ROUND(
                            (
                                SELECT
                                    SUM(
                                        TO_DATE(TO_CHAR(total, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                                        - TO_DATE('01/01/4000 00:00:00', 'DD/MM/YYYY HH24:MI:SS')
                                    ) * 24
                                FROM clocksm1
                                WHERE probsummarym1."NUMBER" = clocksm1.key_char
                                  AND name = 'Pending Customer'
                                GROUP BY key_char
                            ),
                            2
                        ),
                        0
                    ) Pending_customer,
                    CLOSE_TIME,
                    TG_ENLACE_DESTINO,
                    PROBSUMMARYM1.COMPANY
                FROM PROBSUMMARYM1
                INNER JOIN PROBSUMMARYM2
                    ON PROBSUMMARYM1."NUMBER" = PROBSUMMARYM2."NUMBER"
                WHERE PROBSUMMARYM1.assignment IN (
                    'CNOC',
                    'CNOC_CBO_PROACTIVO',
                    'CNOC_CBO_REACTIVO',
                    'CNOC_MASIVO',
                    'GESTION DE DATOS N1',
                    'GESTION N1_CBO',
                    'GT - ACC. EMPRESARIAL - NOC',
                    'SOPORTE_N1_XT',
                    'SOPORTE_N2_XT',
                    'CNOC SGI',
                    'SV - SOPORTE_CORP'
                )
                AND PROBSUMMARYM1."NUMBER" = :FALLA
            )
        SELECT
            LISTADO_TK.*,
            Pending_customer,
            (TOTAL_HORAS - Pending_customer) TOTAL_MENOS_CLIENTE_HORAS,
            TO_CHAR(TRUNC((TOTAL_HORAS - Pending_customer))) || ':' ||
            LPAD(TRUNC(MOD((TOTAL_HORAS - Pending_customer) * 60, 60)), 2, '0') || ':' ||
            LPAD(TRUNC(MOD((TOTAL_HORAS - Pending_customer) * 3600, 60)), 2, '0') AS HH_MM_SS
        FROM LISTADO_TK
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {
            'FALLA': self._normalize_ticket(self.params.get('id', ''))
        }

    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()

        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket

# **********************************************
class MasivasQuery(BaseOracleQuery):
    SQL = """
        WITH
            LISTADO_TK AS (
                SELECT
                    PROBSUMMARYM1."NUMBER" TK,
                    PROBSUMMARYM1.brief_description TITULO,
                    TG_ENLACE,
                    PROBSUMMARYM1.PROBLEM_STATUS,
                    PROBSUMMARYM1.UPDATED_BY ULTIMA_ACTUALIZACION,
                    ASSIGN_DEPT,
                    PROBSUMMARYM1.SYSMODTIME,
                    ROUND((SYSDATE - SYSMODTIME) * 24, 2) TIEMPO_SIN_SEGUIMIENTO_HORAS,
                    TO_CHAR(TRUNC((SYSDATE - SYSMODTIME) * 24)) || ':' ||
                    LPAD(TRUNC(MOD((SYSDATE - SYSMODTIME) * 24 * 60, 60)), 2, '0') || ':' ||
                    LPAD(TRUNC(MOD((SYSDATE - SYSMODTIME) * 24 * 60 * 60, 60)), 2, '0') TIEMPO_SIN_SEGUIMIENTO_F,
                    assignment,
                    opened_by,
                    OPEN_TIME,
                    ROUND((SYSDATE - OPEN_TIME) * 24, 3) AS TOTAL_HORAS,
                    EXTRACT(DAY FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' d ' ||
                    EXTRACT(HOUR FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' h ' ||
                    EXTRACT(MINUTE FROM NUMTODSINTERVAL(SYSDATE - OPEN_TIME, 'DAY')) || ' m' AS TIEMPO_VIDA_TK,
                    FLOOR((SYSDATE - OPEN_TIME) * 24 * 60) AS TOTAL_MINUTOS,
                    NVL(
                        ROUND(
                            (
                                SELECT
                                    SUM(
                                        TO_DATE(TO_CHAR(total, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                                        - TO_DATE('01/01/4000 00:00:00', 'DD/MM/YYYY HH24:MI:SS')
                                    ) * 24
                                FROM clocksm1
                                WHERE probsummarym1."NUMBER" = clocksm1.key_char
                                  AND name = 'Pending Customer'
                                GROUP BY key_char
                            ),
                            2
                        ),
                        0
                    ) Pending_customer,
                    CLOSE_TIME,
                    TG_ENLACE_DESTINO,
                    PROBSUMMARYM1.COMPANY
                FROM PROBSUMMARYM1
                INNER JOIN PROBSUMMARYM2
                    ON PROBSUMMARYM1."NUMBER" = PROBSUMMARYM2."NUMBER"
                WHERE PROBSUMMARYM1.assignment IN (
                    'CNOC',
                    'CNOC_CBO_PROACTIVO',
                    'CNOC_CBO_REACTIVO',
                    'CNOC_MASIVO',
                    'GESTION DE DATOS N1',
                    'GESTION N1_CBO',
                    'GT - ACC. EMPRESARIAL - NOC',
                    'SOPORTE_N1_XT',
                    'SOPORTE_N2_XT',
                    'CNOC SGI',
                    'SV - SOPORTE_CORP'
                )
                AND "CLOSE_TIME" IS NULL
                AND TG_ENLACE LIKE '%MASIV%'
            )
        SELECT
            LISTADO_TK.*,
            Pending_customer,
            (TOTAL_HORAS - Pending_customer) TOTAL_MENOS_CLIENTE_HORAS,
            TO_CHAR(TRUNC((TOTAL_HORAS - Pending_customer))) || ':' ||
            LPAD(TRUNC(MOD((TOTAL_HORAS - Pending_customer) * 60, 60)), 2, '0') || ':' ||
            LPAD(TRUNC(MOD((TOTAL_HORAS - Pending_customer) * 3600, 60)), 2, '0') AS HH_MM_SS
        FROM LISTADO_TK
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {}
