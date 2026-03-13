import oracledb

# activar modo THICK
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_9")


def obtener_conexion():

    conn = oracledb.connect(
        user="frt_msoyos",
        password="Heh-pBH8Mt5u",
        dsn="172.17.114.223/sm9"
    )

    return conn


# prueba directa desde consola
# if __name__ == "__main__":
# 
#     try:
#         conn = obtener_conexion()
#         cursor = conn.cursor()
#         cursor.execute("SELECT SYSDATE FROM dual")
# 
#         for row in cursor:
#             print("Conexion exitosa:", row)
# 
#         cursor.close()
#         conn.close()
# 
#     except Exception as e:
#         print("Error de conexion:", e)