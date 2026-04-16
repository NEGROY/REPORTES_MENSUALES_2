import os
import threading
from pathlib import Path

import oracledb


def _load_env_file(path: str = ".env") -> None:
    """Carga pares KEY=VALUE desde un archivo .env simple si existe."""
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_env_file()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")
ORACLE_CLIENT_LIB = os.getenv("ORACLE_CLIENT_LIB")
ORACLE_POOL_MIN = int(os.getenv("ORACLE_POOL_MIN", "8"))
ORACLE_POOL_MAX = int(os.getenv("ORACLE_POOL_MAX", "50"))
ORACLE_POOL_INC = int(os.getenv("ORACLE_POOL_INC", "5"))
ORACLE_STMT_CACHE_SIZE = int(os.getenv("ORACLE_STMT_CACHE_SIZE", "40"))
ORACLE_FETCH_BATCH_SIZE = int(os.getenv("ORACLE_FETCH_BATCH_SIZE", "1000"))
ORACLE_CALL_TIMEOUT_MS = int(os.getenv("ORACLE_CALL_TIMEOUT_MS", "60000"))

_INIT_CLIENT_ERROR = None
_POOL = None
_POOL_LOCK = threading.Lock()


def _init_client() -> str | None:
    """Inicializa cliente thick si se proporciona ORACLE_CLIENT_LIB."""
    if not ORACLE_CLIENT_LIB:
        return None

    try:
        oracledb.init_oracle_client(lib_dir=ORACLE_CLIENT_LIB)
        return None
    except Exception as exc:
        return f"Error iniciando cliente Oracle: {exc}"


_INIT_CLIENT_ERROR = _init_client()


def _missing_env_vars() -> list[str]:
    return [
        name
        for name, value in (
            ("ORACLE_USER", ORACLE_USER),
            ("ORACLE_PASSWORD", ORACLE_PASSWORD),
            ("ORACLE_DSN", ORACLE_DSN),
        )
        if not value
    ]


def init_pool() -> dict | None:
    global _POOL

    if _INIT_CLIENT_ERROR:
        return {"error": _INIT_CLIENT_ERROR}

    missing = _missing_env_vars()
    if missing:
        return {"error": f"Faltan variables de entorno: {', '.join(missing)}"}

    if _POOL is not None:
        return None

    with _POOL_LOCK:
        if _POOL is not None:
            return None

        try:
            _POOL = oracledb.create_pool(
                user=ORACLE_USER,
                password=ORACLE_PASSWORD,
                dsn=ORACLE_DSN,
                min=ORACLE_POOL_MIN,
                max=ORACLE_POOL_MAX,
                increment=ORACLE_POOL_INC,
                stmtcachesize=ORACLE_STMT_CACHE_SIZE,
            )
            return None

        except oracledb.DatabaseError as e:
            error, = e.args
            return {"error": error.message}


def close_pool() -> None:
    global _POOL

    with _POOL_LOCK:
        if _POOL is not None:
            _POOL.close()
            _POOL = None


def sql_execution(sql: str, tipo: int = 0, parametros: tuple | None = None):
    """
    Ejecuta SQL sobre Oracle.
    tipo 0 = SELECT
    tipo 1 = INSERT/UPDATE
    """
    try:
        pool_error = init_pool()
        if pool_error:
            return pool_error

        with _POOL.acquire() as conn:
            conn.call_timeout = ORACLE_CALL_TIMEOUT_MS

            with conn.cursor() as cursor:
                cursor.arraysize = ORACLE_FETCH_BATCH_SIZE
                cursor.execute(sql, parametros or ())

                if tipo == 1:
                    conn.commit()
                    return {"mensaje": "Operación exitosa"}

                columnas = [col[0] for col in cursor.description]
                resultados = []

                while True:
                    lote = cursor.fetchmany(ORACLE_FETCH_BATCH_SIZE)
                    if not lote:
                        break

                    for fila in lote:
                        fila_dic = {}
                        for col, val in zip(columnas, fila):
                            if isinstance(val, oracledb.LOB):
                                fila_dic[col] = str(val.read())
                            else:
                                fila_dic[col] = val
                        resultados.append(fila_dic)

                return resultados

    except oracledb.DatabaseError as e:
        error, = e.args
        return {"error": error.message}


def oracle_config_status() -> dict:
    return {
        "ORACLE_USER_CONFIGURADO": bool(ORACLE_USER),
        "ORACLE_PASSWORD_CONFIGURADO": bool(ORACLE_PASSWORD),
        "ORACLE_DSN": ORACLE_DSN or "",
        "ORACLE_CLIENT_LIB": ORACLE_CLIENT_LIB or "",
        "ORACLE_POOL_MIN": ORACLE_POOL_MIN,
        "ORACLE_POOL_MAX": ORACLE_POOL_MAX,
        "ORACLE_POOL_INC": ORACLE_POOL_INC,
        "ORACLE_STMT_CACHE_SIZE": ORACLE_STMT_CACHE_SIZE,
        "ORACLE_FETCH_BATCH_SIZE": ORACLE_FETCH_BATCH_SIZE,
        "ORACLE_CALL_TIMEOUT_MS": ORACLE_CALL_TIMEOUT_MS,
        "INIT_CLIENT_ERROR": _INIT_CLIENT_ERROR,
        "POOL_INICIALIZADO": _POOL is not None,
    }


def test_oracle_connection(close_after: bool = True) -> dict:
    try:
        pool_error = init_pool()
        if pool_error:
            return {
                "ok": False,
                "message": "Error al inicializar el pool Oracle.",
                "error": pool_error.get("error", "Error desconocido"),
            }

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

# import os
# import threading
# from pathlib import Path
# import oracledb
# 
# def _load_env_file(path: str = ".env") -> None:
#     """Carga pares KEY=VALUE desde un archivo .env simple si existe."""
#     env_path = Path(path)
#     if not env_path.exists():
#         return
#     for line in env_path.read_text(encoding="utf-8").splitlines():
#         line = line.strip()
#         if not line or line.startswith("#") or "=" not in line:
#             continue
#         key, value = line.split("=", 1)
#         os.environ.setdefault(key.strip(), value.strip())
# 
# _load_env_file()
# 
# ORACLE_USER = os.getenv("ORACLE_USER")
# ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
# ORACLE_DSN = os.getenv("ORACLE_DSN")
# ORACLE_CLIENT_LIB = os.getenv("ORACLE_CLIENT_LIB")  # Ruta del Instant Client si se requiere modo thick
# ORACLE_POOL_MIN = int(os.getenv("ORACLE_POOL_MIN", "8"))
# ORACLE_POOL_MAX = int(os.getenv("ORACLE_POOL_MAX", "50"))
# ORACLE_POOL_INC = int(os.getenv("ORACLE_POOL_INC", "5"))
# ORACLE_STMT_CACHE_SIZE = int(os.getenv("ORACLE_STMT_CACHE_SIZE", "40"))
# ORACLE_FETCH_BATCH_SIZE = int(os.getenv("ORACLE_FETCH_BATCH_SIZE", "1000"))
# ORACLE_CALL_TIMEOUT_MS = int(os.getenv("ORACLE_CALL_TIMEOUT_MS", "60000"))
# 
# def _init_client() -> str | None:
#     """Inicializa cliente thick si se proporciona ORACLE_CLIENT_LIB."""
#     if not ORACLE_CLIENT_LIB:
#         return None
#     try:
#         oracledb.init_oracle_client(lib_dir=ORACLE_CLIENT_LIB)
#         return None
#     except Exception as exc:  # pragma: no cover
#         return f"Error iniciando cliente Oracle: {exc}"
# 
# _INIT_CLIENT_ERROR = _init_client()
# _POOL = None
# _POOL_LOCK = threading.Lock()
# 
# def _missing_env_vars() -> list[str]:
#     return [
#         name
#         for name, value in (
#             ("ORACLE_USER", ORACLE_USER),
#             ("ORACLE_PASSWORD", ORACLE_PASSWORD),
#             ("ORACLE_DSN", ORACLE_DSN),
#         )
#         if not value
#     ]
# 
# def init_pool() -> dict | None:
#     global _POOL
#     if _INIT_CLIENT_ERROR:
#         return {"error": _INIT_CLIENT_ERROR}
# 
#     missing = _missing_env_vars()
#     if missing:
#         return {"error": f"Faltan variables de entorno: {', '.join(missing)}"}
# 
#     if _POOL is not None:
#         return None
# 
#     with _POOL_LOCK:
#         if _POOL is not None:
#             return None
#         try:
#             _POOL = oracledb.create_pool(
#                 user=ORACLE_USER,
#                 password=ORACLE_PASSWORD,
#                 dsn=ORACLE_DSN,
#                 min=ORACLE_POOL_MIN,
#                 max=ORACLE_POOL_MAX,
#                 increment=ORACLE_POOL_INC,
#                 stmtcachesize=ORACLE_STMT_CACHE_SIZE,
#             )
#             return None
#         except oracledb.DatabaseError as e:
#             error, = e.args
#             return {"error": error.message}
# 
# def close_pool() -> None:
#     global _POOL
#     with _POOL_LOCK:
#         if _POOL is not None:
#             _POOL.close()
#             _POOL = None
# 
# def sql_execution(sql: str, tipo: int = 0, parametros: tuple = None):
# 
#     #print(f"Ejecutando SQL: {sql} ")
#     """
#     Ejecuta SQL sobre Oracle. tipo 0 = SELECT, tipo 1 = INSERT/UPDATE.
#     Convierte objetos LOB a string para que sean serializables en JSON
#     """
#     try:
#         pool_error = init_pool()
#         if pool_error:
#             return pool_error
# 
#         with _POOL.acquire() as conn:
#             conn.call_timeout = ORACLE_CALL_TIMEOUT_MS
#             with conn.cursor() as cursor:
#                 cursor.arraysize = ORACLE_FETCH_BATCH_SIZE
#                 cursor.execute(sql, parametros or ())
# 
#                 if tipo == 1:
#                     conn.commit()
#                     return {"mensaje": "Operación exitosa"}
#                 else:
#                     columnas = [col[0] for col in cursor.description]
#                     resultados = []
#                     while True:
#                         lote = cursor.fetchmany(ORACLE_FETCH_BATCH_SIZE)
#                         if not lote:
#                             break
#                         for fila in lote:
#                             fila_dic = {}
#                             for col, val in zip(columnas, fila):
#                                 if isinstance(val, oracledb.LOB):
#                                     fila_dic[col] = str(val.read())
#                                 else:
#                                     fila_dic[col] = val
#                             resultados.append(fila_dic)
#                     return resultados
#     except oracledb.DatabaseError as e:
#         error, = e.args
#         return {"error": error.message}
    
