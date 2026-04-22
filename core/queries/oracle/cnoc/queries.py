from core.queries.oracle.base import BaseOracleQuery


class HistorialDiarioQuery(BaseOracleQuery):
    SQL = """
        WITH
            PARAMETROS AS (
                SELECT
                    :FECHA_INICIO AS FECHA_INICIO,
                    :FECHA_FIN AS FECHA_FIN,
                    :USUARIO AS USUARIO
                FROM DUAL
            ),
            TK AS (
                SELECT
                    "NUMBER" TK
                FROM probsummarym1
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
                AND (
                    CLOSE_TIME IS NULL
                    OR (
                        CLOSE_TIME >= TO_DATE((SELECT FECHA_INICIO FROM PARAMETROS), 'YYYY-MM-DD')
                        AND CLOSE_TIME < TO_DATE((SELECT FECHA_FIN FROM PARAMETROS), 'YYYY-MM-DD')
                    )
                )
            ),
            registros_filtrados AS (
                SELECT
                    SYSMODTIME,
                    "NUMBER"
                FROM ACTIVITYM1
                WHERE "NUMBER" IN (SELECT TK FROM TK)
                  AND TYPE = 'Actualización Cliente'
                  AND OPERATOR = (SELECT USUARIO FROM PARAMETROS)
                  AND (
                        SYSMODTIME >= TO_DATE((SELECT FECHA_INICIO FROM PARAMETROS), 'YYYY-MM-DD')
                    AND SYSMODTIME < TO_DATE((SELECT FECHA_FIN FROM PARAMETROS), 'YYYY-MM-DD')
                  )
                ORDER BY SYSMODTIME
            )
        SELECT
            interval_start,
            LISTAGG("NUMBER", ', ') WITHIN GROUP (ORDER BY "NUMBER") AS tickets_unicos,
            COUNT(*) AS total
        FROM (
            SELECT
                "NUMBER",
                TRUNC(SYSMODTIME, 'DD')
                + (TRUNC((SYSMODTIME - TRUNC(SYSMODTIME, 'DD')) * 48) / 48) AS interval_start
            FROM registros_filtrados
        )
        GROUP BY interval_start
        ORDER BY interval_start
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {
            'FECHA_INICIO': self.params.get('fecha_inicio', ''),
            'FECHA_FIN': self.params.get('fecha_fin', ''),
            'USUARIO': self.params.get('operador', ''),
        }

# ------------------------------
# Endpoint 11: # http://127.0.0.1:8080/buscar_tk/F6433510
# ------------------------------
class BusquedaTkQuery(BaseOracleQuery):
    SQL = """
        WITH
            lista_de_tickets AS (
                SELECT
                    probsummarym1."NUMBER"       ticket,
                    problem_type,
                    open_time                    "FECHA DE APERTURA",
                    probsummarym1.close_time     "FECHA DE CIERRE",
                    resolved_group               "GRUPO QUE RESOLVIO",
                    tg_enlace                    enlace,
                    company                      cliente,
                    category                     falla,
                    subcategory                  subfalla,
                    close_time - open_time       "TIEMPO VIDA TICKET",
                    probsummarym1.assignment     "GRUPO ASIGNADO",
                    assignee_name                "GESTOR",
                    (
                        to_date(to_char(close_time, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                        - to_date(to_char(open_time, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                    ) * 24 AS "TIEMPO VIDA TICKET (horas)",
                    problem_status,
                    variable3,
                    PROBSUMMARYM2.res_anal_code,
                    UPDATE_ACTION ULTIMO_COMENTARIO,
                    TG_ULTIMOSEGUIMIENTO as UPDATE_ACTION,
                    TG_ENLACE
                FROM
                    probsummarym1,
                    probsummarym2
                WHERE
                        probsummarym1."NUMBER" = probsummarym2."NUMBER"
                    AND probsummarym1.ASSIGNMENT IN (
                        'GESTION DE DATOS N1',
                        'GESTION N1_CBO',
                        'CNOC_CBO_PROACTIVO',
                        'CNOC_CBO_REACTIVO',
                        'CNOC',
                        'GT - ACC. EMPRESARIAL - NOC',
                        'CNOC_NICARAGUA'
                    )
                    AND probsummarym1.close_time IS NULL
            ),
            ACTUALIZACION AS (
                SELECT
                    "NUMBER" AS TICKET,
                    ASSIGN_MAX_T F_ULTMA_ASIGNACION,
                    ASSIGN_USER_ULT U_ULTMA_ASIGNACION,
                    AC_CLI_MAX_T F_ACTUALIZACION_CLIENTE,
                    AC_CLI_USER_ULT ACTUALIZACION_CLIENTE,
                    UPD_MAX_T F_UPDATE,
                    UPD_USER_ULT UPDATE_USUARIO,
                    ESCAL_MAX_T F_ESCALACION,
                    ESCAL_USER_ULT F_USUARIO_ESCALACION
                FROM (
                    SELECT
                        "NUMBER",
                        CASE
                            WHEN UPPER(type) = 'ACTUALIZACION CLIENTE' THEN 'Actualizacion Cliente'
                            WHEN UPPER(type) = 'ASSIGNMENT' THEN 'Assignment'
                            WHEN UPPER(type) LIKE '%ESCALACION%' THEN 'Escalación'
                            WHEN UPPER(type) = 'UPDATE' THEN 'Update'
                        END AS criterio,
                        sysmodtime,
                        sysmoduser
                    FROM ACTIVITYM1
                    WHERE "NUMBER" IN (SELECT ticket FROM lista_de_tickets)
                      AND (
                            UPPER(type) IN ('ACTUALIZACION CLIENTE', 'ASSIGNMENT', 'UPDATE')
                         OR UPPER(type) LIKE '%ESCALACION%'
                      )
                ) src
                PIVOT (
                    MAX(sysmodtime) AS MAX_T,
                    MAX(sysmoduser) KEEP (DENSE_RANK LAST ORDER BY sysmodtime) AS USER_ULT
                    FOR criterio IN (
                        'Assignment'            AS ASSIGN,
                        'Actualizacion Cliente' AS AC_CLI,
                        'Update'                AS UPD,
                        'Escalación'            AS ESCAL
                    )
                )
                ORDER BY TICKET
            ),
            complementario AS (
                SELECT
                    A.*,
                    SYSDATE,
                    ROUND(((SYSDATE - F_ACTUALIZACION_CLIENTE) * 1440) / 60, 2) ACTUALIZACION_C_SIN_ACTULIZAR,
                    ROUND(((SYSDATE - F_UPDATE) * 1440) / 60, 2) SIN_ACTULIZAR_TK,
                    CASE
                        WHEN (SYSDATE - F_ACTUALIZACION_CLIENTE) >= 1 THEN
                            TRUNC(SYSDATE - F_ACTUALIZACION_CLIENTE) || ' dias, ' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_ACTUALIZACION_CLIENTE) * 24, 24)), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_ACTUALIZACION_CLIENTE) * 1440, 60)), 2, '0')
                        ELSE
                            LPAD(TRUNC((SYSDATE - F_ACTUALIZACION_CLIENTE) * 24), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_ACTUALIZACION_CLIENTE) * 1440, 60)), 2, '0')
                    END AS ACTUAL_C_SIN_ACTUALIZAR_TXT,
                    CASE
                        WHEN (SYSDATE - F_UPDATE) >= 1 THEN
                            TRUNC(SYSDATE - F_UPDATE) || ' dias, ' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_UPDATE) * 24, 24)), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_UPDATE) * 1440, 60)), 2, '0')
                        ELSE
                            LPAD(TRUNC((SYSDATE - F_UPDATE) * 24), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_UPDATE) * 1440, 60)), 2, '0')
                    END AS SIN_ACTUALIZAR_TK_TXT
                FROM ACTUALIZACION A
            )
        SELECT
            complementario.*,
            lista_de_tickets.FALLA,
            lista_de_tickets.PROBLEM_STATUS,
            lista_de_tickets."GRUPO ASIGNADO",
            lista_de_tickets.variable3,
            lista_de_tickets.UPDATE_ACTION,
            lista_de_tickets.tg_enlace,
            lista_de_tickets.GESTOR
        FROM complementario
        INNER JOIN lista_de_tickets
            ON lista_de_tickets.TICKET = complementario.TICKET
        WHERE lista_de_tickets.TICKET = :TICKET
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {
            'TICKET': self._normalize_ticket(self.params.get('falla_id', ''))
        }

    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()

        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket

# ------------------------------
# Endpoint 9: # AGREGARLE CONSULTA PARA TRAER TODAS LAS FALLAS ABIERTAS Y SIN SEGUIMEINTO 
# http://127.0.0.1:8000/api/cnoc/ultimo_seguimeinto/
# ------------------------------
class UltimoSeguimientoQuery(BaseOracleQuery):
    SQL = """
        WITH
            lista_de_tickets AS (
                SELECT
                    probsummarym1."NUMBER" ticket,
                    problem_type,
                    open_time "FECHA DE APERTURA",
                    probsummarym1.close_time "FECHA DE CIERRE",
                    resolved_group "GRUPO QUE RESOLVIO",
                    tg_enlace enlace,
                    company cliente,
                    category falla,
                    subcategory subfalla,
                    close_time - open_time "TIEMPO VIDA TICKET",
                    probsummarym1.assignment "GRUPO ASIGNADO",
                    assignee_name "GESTOR",
                    (
                        to_date(to_char(close_time, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                        - to_date(to_char(open_time, 'DD/MM/YYYY HH24:MI:SS'), 'DD/MM/YYYY HH24:MI:SS')
                    ) * 24 AS "TIEMPO VIDA TICKET (horas)",
                    problem_status,
                    variable3,
                    PROBSUMMARYM2.res_anal_code,
                    UPDATE_ACTION ULTIMO_COMENTARIO,
                    TG_ULTIMOSEGUIMIENTO as UPDATE_ACTION,
                    TG_ENLACE
                FROM
                    probsummarym1,
                    probsummarym2
                WHERE
                        probsummarym1."NUMBER" = probsummarym2."NUMBER"
                    AND probsummarym1.ASSIGNMENT IN (
                        'GESTION DE DATOS N1',
                        'GESTION N1_CBO',
                        'CNOC_CBO_PROACTIVO',
                        'CNOC_CBO_REACTIVO',
                        'CNOC',
                        'GT - ACC. EMPRESARIAL - NOC',
                        'CNOC_NICARAGUA'
                    )
                    AND probsummarym1.close_time IS NULL
            ),
            ACTUALIZACION AS (
                SELECT
                    "NUMBER" AS TICKET,
                    ASSIGN_MAX_T F_ULTMA_ASIGNACION,
                    ASSIGN_USER_ULT U_ULTMA_ASIGNACION,
                    AC_CLI_MAX_T F_ACTUALIZACION_CLIENTE,
                    AC_CLI_USER_ULT ACTUALIZACION_CLIENTE,
                    UPD_MAX_T F_UPDATE,
                    UPD_USER_ULT UPDATE_USUARIO,
                    ESCAL_MAX_T F_ESCALACION,
                    ESCAL_USER_ULT F_USUARIO_ESCALACION
                FROM (
                    SELECT
                        "NUMBER",
                        CASE
                            WHEN UPPER(type) = 'ACTUALIZACION CLIENTE' THEN 'Actualizacion Cliente'
                            WHEN UPPER(type) = 'ASSIGNMENT' THEN 'Assignment'
                            WHEN UPPER(type) LIKE '%ESCALACION%' THEN 'Escalación'
                            WHEN UPPER(type) = 'UPDATE' THEN 'Update'
                        END AS criterio,
                        sysmodtime,
                        sysmoduser
                    FROM ACTIVITYM1
                    WHERE "NUMBER" IN (SELECT ticket FROM lista_de_tickets)
                      AND (
                            UPPER(type) IN ('ACTUALIZACION CLIENTE', 'ASSIGNMENT', 'UPDATE')
                         OR UPPER(type) LIKE '%ESCALACION%'
                      )
                ) src
                PIVOT (
                    MAX(sysmodtime) AS MAX_T,
                    MAX(sysmoduser) KEEP (DENSE_RANK LAST ORDER BY sysmodtime) AS USER_ULT
                    FOR criterio IN (
                        'Assignment'            AS ASSIGN,
                        'Actualizacion Cliente' AS AC_CLI,
                        'Update'                AS UPD,
                        'Escalación'            AS ESCAL
                    )
                )
                ORDER BY TICKET
            ),
            complementario AS (
                SELECT
                    A.*,
                    SYSDATE,
                    ROUND(((SYSDATE - F_ACTUALIZACION_CLIENTE) * 1440) / 60, 2) ACTUALIZACION_C_SIN_ACTULIZAR,
                    ROUND(((SYSDATE - F_UPDATE) * 1440) / 60, 2) SIN_ACTULIZAR_TK,
                    CASE
                        WHEN (SYSDATE - F_ACTUALIZACION_CLIENTE) >= 1 THEN
                            TRUNC(SYSDATE - F_ACTUALIZACION_CLIENTE) || ' dias, ' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_ACTUALIZACION_CLIENTE) * 24, 24)), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_ACTUALIZACION_CLIENTE) * 1440, 60)), 2, '0')
                        ELSE
                            LPAD(TRUNC((SYSDATE - F_ACTUALIZACION_CLIENTE) * 24), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_ACTUALIZACION_CLIENTE) * 1440, 60)), 2, '0')
                    END AS ACTUAL_C_SIN_ACTUALIZAR_TXT,
                    CASE
                        WHEN (SYSDATE - F_UPDATE) >= 1 THEN
                            TRUNC(SYSDATE - F_UPDATE) || ' dias, ' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_UPDATE) * 24, 24)), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_UPDATE) * 1440, 60)), 2, '0')
                        ELSE
                            LPAD(TRUNC((SYSDATE - F_UPDATE) * 24), 2, '0') || ':' ||
                            LPAD(TRUNC(MOD((SYSDATE - F_UPDATE) * 1440, 60)), 2, '0')
                    END AS SIN_ACTUALIZAR_TK_TXT
                FROM ACTUALIZACION A
            )
        SELECT
            complementario.*,
            lista_de_tickets.FALLA,
            lista_de_tickets.PROBLEM_STATUS,
            lista_de_tickets."GRUPO ASIGNADO",
            lista_de_tickets.variable3,
            lista_de_tickets.UPDATE_ACTION,
            lista_de_tickets.tg_enlace,
            lista_de_tickets.GESTOR
        FROM complementario
        INNER JOIN lista_de_tickets
            ON lista_de_tickets.TICKET = complementario.TICKET
        WHERE lista_de_tickets.TG_ENLACE NOT LIKE '%MASIVO%'
        ORDER BY complementario.F_ACTUALIZACION_CLIENTE DESC
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {}

# ------------------------------
# Endpoint 10: # http://127.0.0.1:8080/cronologia?falla_id=F6433510
# http://172.20.97.102:8080/cronologia/F6840709
# ------------------------------
# DEFINIMOS LA CLASE DE CRONOLOGIA, para reutilziar la baseOracleQuery
# CronologiaQuery(params={'ticket': '12345'})
class CronologiaQuery(BaseOracleQuery):
    # CADENA ESTATICA DE SQL 
    SQL = """
        SELECT
            UPDATE_ACTION AS ULTIMO_COMENTARIO,
            "NUMBER",
            OPEN_TIME,
            CLOSE_TIME
        FROM probsummarym1
        WHERE "NUMBER" = :TICKET
    """
    # METODO REQUERIDO, ejecuta la query 
    def get_sql(self) -> str:
        return self.SQL

    # dicciionario, con los parametros de SQL 
    def get_params(self) -> dict:
        return {
            'TICKET': self._normalize_ticket(self.params.get('ticket', ''))
        }
    # apoya para el SRP, encapsula la logica de limpieza. 
    def _normalize_ticket(self, ticket: str) -> str:
        ticket = (ticket or '').replace(' ', '').upper()
        # si no empieza por F SE LA COLOCA 
        if ticket and not ticket.startswith('F'):
            ticket = f'F{ticket}'

        return ticket

# ------------------------------
# Endpoint 6: ENDPOINT PARA EL EXCEL en get TRAE DE LA TB  probsummarym1 
# http://127.0.0.1:8000/api/cnoc/tickets/
# ------------------------------
class TicketsCnocQuery(BaseOracleQuery):
    SQL = """
        SELECT
            m1.UPDATE_TIME,
            TO_CHAR(m1.UPDATE_TIME, 'hh24:mi') "Hora",
            m1."NUMBER",
            m1.ASSIGNEE_NAME,
            m1.COMPANY,
            m2.TG_ENLACE,
            m1.COUNTRY,
            m1.assignment,
            m1.PROBLEM_STATUS,
            TG_ULTIMOSEGUIMIENTO AS UPDATE_ACTION,
            VARIABLE3,
            m2.TG_ACTIVIDAD_PENDIENTE,
            m2.INITIAL_IMPACT,
            m1.HOT_TIC
        FROM probsummarym1 m1
        INNER JOIN probsummarym2 m2
            ON m1."NUMBER" = m2."NUMBER"
        WHERE m1.ASSIGNMENT IN (
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
        AND m1.CLOSE_TIME IS NULL
    """

    def get_sql(self) -> str:
        return self.SQL

    def get_params(self) -> dict:
        return {}

# 


#


#


#


#


#