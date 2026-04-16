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


def get_pool():
    return _POOL


def close_pool() -> None:
    global _POOL

    with _POOL_LOCK:
        if _POOL is not None:
            _POOL.close()
            _POOL = None


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