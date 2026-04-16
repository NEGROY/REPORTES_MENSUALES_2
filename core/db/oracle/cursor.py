from contextlib import contextmanager

from .connection import (
    ORACLE_CALL_TIMEOUT_MS,
    ORACLE_FETCH_BATCH_SIZE,
    get_pool,
    init_pool,
)


@contextmanager
def oracle_connection():
    pool_error = init_pool()
    if pool_error:
        raise RuntimeError(pool_error.get("error", "Error al inicializar pool Oracle."))

    pool = get_pool()
    if pool is None:
        raise RuntimeError("No fue posible obtener el pool Oracle.")

    with pool.acquire() as conn:
        conn.call_timeout = ORACLE_CALL_TIMEOUT_MS
        yield conn


@contextmanager
def oracle_cursor():
    with oracle_connection() as conn:
        with conn.cursor() as cursor:
            cursor.arraysize = ORACLE_FETCH_BATCH_SIZE
            yield conn, cursor
