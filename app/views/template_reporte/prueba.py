from django.shortcuts import render
from datetime import datetime
import time

from app.service.conexion import obtener_conexion
from app.service.reportes_sql import historico_de_indicadores
from app.service.funciones import ultimos_6_meses
from app.service.PAG_func import get_pag_General, get_pag_MesActual

from app.models.empresas_catalogo import EmpresasCatalogo
from app.models.pag_reporte import PagReporte
# **********************************************************************

# Define qué páginas usan qué función
PAGINAS_CONFIG = {
    "pag_5": "actual",
    "pag_7": "actual",
    "pag_8": "actual",
    "pag_9": "5meses",
    "pag_10": "5meses",
    "pag_11": "5meses",
    "pag_12": "5meses",
    "pag_13": "5meses",
    "pag_14": "actual",
    "pag_15": "5meses",
    "pag_16": "5meses",
    "pag_17": "actual",
    "pag_18": "actual",
    "pag_19": "5meses",
    "pag_20": "actual",
}

#DEFINIMOS LOS MESES 
# DEFINIMOS LOS MESES
meses_nombre = {
    "01": "ENERO",
    "02": "FEBRERO",
    "03": "MARZO",
    "04": "ABRIL",
    "05": "MAYO",
    "06": "JUNIO",
    "07": "JULIO",
    "08": "AGOSTO",
    "09": "SEPTIEMBRE",
    "10": "OCTUBRE",
    "11": "NOVIEMBRE",
    "12": "DICIEMBRE"
}

# REALIZA LA CREACION DE LOS NOMBRES DE LOS TEMPLATES Y PAG
def obtener_paginas_templates(id_empresa):
    # LISTA DEFAULT
    paginas_default = list(range(1, 21))
    # ==========================
    # VALIDAR ID EMPRESA
    if not id_empresa:
        paginas = paginas_default
        print("EMPRESA VACÍA → usando páginas por default")
    else:
        id_empresa = int(id_empresa)

        registro = PagReporte.objects.filter(
            id_cliente=id_empresa,
            estado=True
        ).first()
        # ==========================
        # VALIDAR RESULTADO
        if not registro:
            print("SIN REGISTRO → usando páginas por default")
            paginas = paginas_default
        elif isinstance(registro.paginas, list) and registro.paginas:
            paginas = registro.paginas
        else:
            print("REGISTRO SIN PÁGINAS VÁLIDAS → usando página 3")
            paginas = [3]
    # ==========================
    # FILTRAR (máximo hasta 10)
    paginas_filtradas = [p for p in paginas if p <= 21]
    # ==========================
    # TEMPLATES
    paginas_templates = [
        f"paginas/pag{p}.html"
        for p in paginas_filtradas
    ]
    # ==========================
    # NOMBRES PARA LÓGICA pag_1, pag2....
    paginas_nombres = [
        f"pag_{p}"
        for p in paginas_filtradas
    ]

    return {
        "templates": paginas_templates,
        "nombres": paginas_nombres
    }

# FUNCION PARA OBTENER TODOS LOS DATOS DE LAS PAGINAS
def generar_paginas_data(paginas_nombres, PAGINAS_CONFIG, datosPag, cadena_mes):
    # PAGINAS 
    paginas_data = {}

    for nombre_pag in paginas_nombres:
        # Validar configuración de la página
        tipo = PAGINAS_CONFIG.get(nombre_pag)
        if not tipo:
            # Ej: páginas sin query (pag_1, pag_2, etc.)
            continue
        try:
            print(f" EJECUTANDO CONSULTA: {nombre_pag}... {tipo}")
            time.sleep(0.5)  # medio segundo entre queries
            if tipo == "actual":
                resultado = get_pag_MesActual(datosPag, nombre_pag)
            elif tipo == "5meses":
                resultado = get_pag_General(datosPag, cadena_mes, nombre_pag)
            else:
                print(f" Tipo no reconocido en {nombre_pag}")
                resultado = None
            paginas_data[nombre_pag] = resultado
            print(f"✅ Finalizó {nombre_pag}")

        except Exception as e:
            print(f"❌ Error en {nombre_pag}: {e}")
            paginas_data[nombre_pag] = None  # evita que rompa todo

    return paginas_data
     
# http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=03&anio=2026&total_enlaces=55
def reporte_prueba(request):

     # FECHA ACTUAL ***********************************
    hoy = datetime.now()
    mes_actual = hoy.strftime("%m")
    anio_actual = hoy.strftime("%Y")
    # PARAMETROS    ***********************************
    id_empresa = request.GET.get("empresa")
    mes = request.GET.get("mes")        # MARZO, ENERO, FEBREO
    anio = request.GET.get("anio")
    total_enlaces = request.GET.get("total_enlaces")

    # -----------------------------
    # VALIDACIONES
    # EMPRESA || SI ESTA VACIA QUE SEA 3 (PRUEBAS POR DEFAULT )
    if not id_empresa:
        id_empresa = "3"
    else:
        id_empresa = int(id_empresa)
    # MES ||  si esta vacio tomma el mes actual 
    if not mes or not mes.isdigit() or len(mes) > 2 or int(mes) < 1 or int(mes) > 12:
        mes = mes_actual
    else:
        mes = mes.zfill(2)
    # AÑO ||  si esta vacio tomma el AÑO actual 
    if not anio or not anio.isdigit():
        anio = anio_actual
    # TOTAL ENLACES
    if not total_enlaces or not total_enlaces.isdigit():
        total_enlaces = 1
    else:
        total_enlaces = int(total_enlaces)

    # -----------------------------
    # 1) OBTENEMOS todas las paginas  ['paginas/pag1.html'])
    # AGREGAR UNA VALIDACION SI LA EMPRESA ES MENSUAL ENVIAR VACIO
    paginas = obtener_paginas_templates(id_empresa)

    # -----------------------------
    # 2) OBTIENE LOS DATOS DE LA EMPRESA 
    empresa = None
    if id_empresa:
        empresa = EmpresasCatalogo.objects.get(COD=id_empresa)
        # VALIDAR SI CAMBIO TOTAL ENLACES
        if total_enlaces:
            total_enlaces = int(total_enlaces)

            if empresa.tt_sitioa != total_enlaces:
                empresa.tt_sitioa = total_enlaces
                empresa.save(update_fields=["tt_sitioa"])

    # CONSULTA ORACLE INICICIO 
    conn = obtener_conexion()
    cursor = conn.cursor()
    #---------------------------------------------------
    # 4.1) FUNCION PARA CALCULAR LOS ULTIMOS 6 MESES 
    meses = ultimos_6_meses(int(mes), int(anio))
    nombre_mes = meses_nombre[mes]

    # 3) CREA LOS CAMPOS DE DATOS DESDE empresa
    data = {
        "titulo": "REPORTE MONITOREO",
        "nombre": str(empresa) if empresa else "CLIENTE DEMO",
        "mes": mes,
        "anio": anio,
        "sitios": total_enlaces,
        "nombre": empresa,
    }
    # 4.2) CASE DE PAIS ABREVISATURAS 
    pais_abrev = {
        "GT": "GUATEMALA",
        "SV": "EL SALVADOR",
        "HN": "HONDURAS",
        "NI": "NICARAGUA",
        "CR": "COSTA RICA",
        "CENAM": "CENAM"
    }
    paisComplete = pais_abrev.get(empresa.pais, empresa.pais)
    # 4)  EMPEZAMOS A CREAR LOS DATOS PARA LAS PAGINAS 
    datosPag= {
        "date_ini": meses["FECHA_INI"],
        "date_end": meses["FECHA_FIN"],
        "where_tk": empresa.donde,
        "pais": empresa.pais,
        "paiscomplete": paisComplete,
        "companya": empresa.razon_social,
        "mes": mes,
        "anio": anio, 
        "date_ini_5": meses["FECHA_INI_5"],
        "HRSxMES" : meses["HRSxMES"],
    }
    # CADENAS DE MESE PARA LAS CONSULTAS DE 5 MESES 
    cadena_mes = ",".join(meses[f"MESN_{i}"] for i in range(5, 0, -1)) + "," + meses["MESN"]

    # FUNCION PARA OBTENER TODOS LOS DATOS DE LAS PAGINAS SELECCIONADAS 
    paginas_nombres = paginas["nombres"]
    paginas_data = generar_paginas_data(paginas_nombres, PAGINAS_CONFIG, datosPag, cadena_mes)

    # ========================== 
    return render(
        request,
        "template_reporte/Mensuales.html",
        {
            "id": 1 ,
            "data": data,
            "meses": meses,
            # "hi_indi": resultados,
            # "sql": sql,
            # "empresa": empresa,
            "mes": nombre_mes,
            "anio": anio,
            "paginas": paginas,
            "paginas_data": paginas_data , 
        }
    )

#http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=MARZO&anio=2026&total_enlaces=55