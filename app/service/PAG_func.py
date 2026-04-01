import json
import os
from datetime import datetime, timedelta
import oracledb
from datetime import datetime

from app.service.conexion import obtener_conexion
# TRAE TODO  # from app.service.reportes_sql import ( pagina_5, pagina_7, pag_8, pag_9, pag_10, pag_11)
from app.service.reportes_sql import *

# VAMOS A EMPEZAR A REALIZAR las FUNCIONES DE LAS  PAGINAS 
FUNCIONES_SQL = {
    "pag_5":  pag_5,    #"actual"
    "pag_7":  pag_7,    #"actual"
    "pag_8":  pag_8,    #"5meses"
    "pag_9":  pag_9,    # "actual
    "pag_10": pag_10,  # "5meses
    "pag_11": pag_11,  # "5meses
    "pag_12": pag_12,  # "5meses
    "pag_13": pag_13,  # "5meses
    "pag_14": pag_14,  # "5meses 
    "pag_15": pag_15,  # "actual
    "pag_16": pag_16,  # "5meses
    "pag_17": pag_17,  # "5meses 
    "pag_18": pag_18,  # "actual  
    "pag_19": pag_19,  # "actual
    "pag_20": pag_20,  # "5meses    
    "pag_21": pag_21,  # "actual    
    "pag_22": pag_22,  # "5meses  
    "pag_23": pag_23,  # "5meses                
}

# PAGINA 5
# ==============================
def get_pag5(datosp5):  

    date_ini = datosp5["date_ini"]
    date_end = datosp5["date_end"]
    where_tk = datosp5["where_tk"]
    pais = datosp5["pais"]
    paiscomplete = datosp5["paiscomplete"]
 
    sql = pagina_5(date_ini, date_end, where_tk, pais, paiscomplete)     #  print(sql)
    
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
# ==============================
# Causas Monitoreo Reactivo Atribuibles al Cliente PAG 11
def get_pag11(datosPag, cadena_mes):

    date_ini = datosPag["date_ini_5"]
    date_end = datosPag["date_end"]
    where_tk = datosPag["where_tk"]
    pais = datosPag["pais"]
    paiscomplete = datosPag["paiscomplete"]
    
    sql = pag_11(date_ini, date_end, where_tk, pais, paiscomplete, cadena_mes )#     print(sql)

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
# **********************************************************
# EVENTUALMENTE ELIMINAREMOS TODO LO ANTERIORIOR
# **********************************************************

# ==============================
# DEBIDO A QUE LAS ULTIMAS 3 FUNCIONES SON IDENTICAS VAMOS A CREAR UNA GENERAL 
# ESTA FUNCION SOLO SIRVE CUANDO INICIO ES HACE 5 MESES Y FIN ES EL MES ACTUAL 
def get_pag_General(datosPag, cadena_mes, func_sql ):
    #   convertir string a función
    if isinstance(func_sql, str):
        func_sql = FUNCIONES_SQL.get(func_sql)

        if not func_sql:
            raise ValueError(f"Función SQL no válida: {func_sql}")
        
    # OBTENMOS LOS DATOS 
    date_ini = datosPag["date_ini_5"]
    date_end = datosPag["date_end"]
    where_tk = datosPag["where_tk"]
    pais = datosPag["pais"]
    paiscomplete = datosPag["paiscomplete"]
    cadena_anio = datosPag["cadena_anio"]

    sql = func_sql(date_ini, date_end, where_tk, pais, paiscomplete, cadena_mes, cadena_anio) #    print(sql)
    # with open("consulta.sql.txt", "a", encoding="utf-8") as f:
    #     f.write(sql)
    #     f.write("\n")


    with obtener_conexion() as conn:
        with conn.cursor() as cursor:
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

    return datos      

# ==============================
# FUNCION GENERAL PARA EL MES ACTUAL 
# FUNCION PARA CONSULTAS DEL MES SELECCIONADO, 
def get_pag_MesActual(datosPag, func_sql):
    date_ini = datosPag["date_ini"]
    date_end = datosPag["date_end"]
    # fecha_fin = ( datetime.strptime(date_end, "%d%m%Y") + timedelta(days=1) ).strftime("%d%m%Y") #    print(fecha_fin)
    where_tk = datosPag["where_tk"]
    pais = datosPag["pais"]
    paiscomplete = datosPag["paiscomplete"]
    
    #  convertir string a función
    if isinstance(func_sql, str):
        func_sql = FUNCIONES_SQL.get(func_sql)

        if not func_sql:
            raise ValueError(f"Función SQL no válida: {func_sql}")
    #CONSULTA CONTATENADA 
    sql = func_sql(date_ini, date_end, where_tk, pais, paiscomplete ) #     print(func_sql)
    # with open("consulta.sql.txt", "a", encoding="utf-8") as f:
    #     f.write(sql)
    #     f.write("\n")


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



# ==============================