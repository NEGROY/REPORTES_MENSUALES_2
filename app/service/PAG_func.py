import json
import os
import oracledb
from datetime import datetime

from app.service.conexion import obtener_conexion
from app.service.reportes_sql import pagina_5, pagina_7, pag_8

# VAMOS A EMPEZAR A REALIZAR las FUNCIONES DE LAS  PAGINAS 

# ==============================
# PAGINA 5
# ==============================
def get_pag5(datosp5):

    date_ini = datosp5["date_ini"]
    date_end = datosp5["date_end"]
    where_tk = datosp5["where_tk"]
    pais = datosp5["pais"]
    paiscomplete = datosp5["paiscomplete"]
 
    sql = pagina_5(date_ini, date_end, where_tk, pais, paiscomplete)
    #  print(sql)
    #  print("================================")
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(sql)
    columnas = [col[0] for col in cursor.description]

    datos = []
    for fila in cursor:
        fila_dict = {}
        for col, val in zip(columnas, fila):
            if isinstance(val, oracledb.LOB):
                fila_dict[col] = val.read()
            elif isinstance(val, datetime):
                fila_dict[col] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                fila_dict[col] = val
        datos.append(fila_dict)

    cursor.close()
    conn.close()

    return datos
 
# ==============================
# PAGINA 7 
def get_pag7(datosPag):
    date_ini = datosPag["date_ini"]
    date_end = datosPag["date_end"]
    where_tk = datosPag["where_tk"]
    pais = datosPag["pais"]
    paiscomplete = datosPag["paiscomplete"]

    mes  = datosPag["mes"]
    anio = datosPag["anio"]
    
    # HAY QUE VALIDAR QUE LOS DATOS ESTEN LA BD 
    # Y ASGREARLOS SI NO EXISTE SQUE MUESTRE LOS HI INIDCADORES QUER SE TIENEN 

    sql = pagina_7(date_ini, date_end, where_tk, pais, paiscomplete, mes, anio)
    print(sql)

    return sql

# ==============================
# Distribución de Incidentes pagina 8 
def get_pag8(datosPag):
    date_ini = datosPag["date_ini"]
    date_end = datosPag["date_end"]
    where_tk = datosPag["where_tk"]
    pais = datosPag["pais"]
    paiscomplete = datosPag["paiscomplete"]

    sql = pag_8(date_ini, date_end, where_tk, pais, paiscomplete )
    print(sql)

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(sql)
    columnas = [col[0] for col in cursor.description]

    datos = []
    for fila in cursor:
        fila_dict = {}
        for col, val in zip(columnas, fila):
            if isinstance(val, oracledb.LOB):
                fila_dict[col] = val.read()
            elif isinstance(val, datetime):
                fila_dict[col] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                fila_dict[col] = val
        datos.append(fila_dict)

    cursor.close()
    conn.close()

    return datos