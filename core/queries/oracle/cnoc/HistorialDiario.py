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
