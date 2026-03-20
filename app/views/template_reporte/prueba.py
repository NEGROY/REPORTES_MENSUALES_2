from django.shortcuts import render
from datetime import datetime
 #  SERVICIOS
from app.service.conexion import obtener_conexion
from app.service.funciones import *
 #  MODELOS
from app.models.empresas_catalogo import EmpresasCatalogo
 

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
        "parque_where": empresa.parque_where,
        "pais": empresa.pais,
        "paiscomplete": paisComplete,
        "companya": empresa.razon_social,
        "mes": mes,
        "anio": anio, 
        "empresa": id_empresa,
        "date_ini_5": meses["FECHA_INI_5"],
        "HRSxMES" : meses["HRSxMES"],
    }
    # CADENAS DE MESE PARA LAS CONSULTAS DE 5 MESES 
    cadena_mes = ",".join(meses[f"MESN_{i}"] for i in range(5, 0, -1)) + "," + meses["MESN"]

    #DATOS DE LOS HI HISTORICOS INDICADORES 
    hi_indi= obtener_historico_indicadores( conn, datosPag )
    hi_indi = normalizar_dinamico(hi_indi)
    
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
            "hi_indi": hi_indi,
            # "sql": sql,
            # "empresa": empresa,
            "mes": nombre_mes,
            "anio": anio,
            "paginas": paginas,
            "paginas_data": paginas_data , 
        }
    )

#http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=MARZO&anio=2026&total_enlaces=55