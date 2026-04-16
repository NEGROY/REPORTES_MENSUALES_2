import oracledb

from .cursor import oracle_cursor


def sql_execution(sql: str, tipo: int = 0, parametros: tuple | None = None):
    """
    Ejecuta SQL sobre Oracle.
    tipo 0 = SELECT
    tipo 1 = INSERT/UPDATE
    """
    try:
        with oracle_cursor() as (conn, cursor):
            cursor.execute(sql, parametros or ())

            if tipo == 1:
                conn.commit()
                return {"mensaje": "Operación exitosa"}

            columnas = [col[0] for col in cursor.description] if cursor.description else []
            resultados = []

            while True:
                lote = cursor.fetchmany(cursor.arraysize)
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
    except Exception as exc:
        return {"error": str(exc)}