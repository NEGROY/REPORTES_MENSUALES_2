from .connection import close_pool
from .queries import sql_execution


def test_oracle_connection(close_after: bool = True) -> dict:
    try:
        result = sql_execution(
            """
            SELECT
                'CONEXION_OK' AS ESTADO,
                TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') AS FECHA_SERVIDOR
            FROM DUAL
            """
        )

        if isinstance(result, dict) and result.get("error"):
            return {
                "ok": False,
                "message": "Error al ejecutar consulta de prueba.",
                "error": result["error"],
            }

        row = result[0] if result else {}

        return {
            "ok": True,
            "message": "Conexión Oracle exitosa.",
            "data": row,
        }

    except Exception as exc:
        return {
            "ok": False,
            "message": "Error inesperado al probar Oracle.",
            "error": str(exc),
        }

    finally:
        if close_after:
            close_pool()