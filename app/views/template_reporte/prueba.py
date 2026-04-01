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
    # print(paginas)

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
    #titulos concatenada
    titulo = (
        f"REPORTE CNOC - {nombre_mes} {anio} - "
        f"{empresa.razon_social}  "
    )

    # 3) CREA LOS CAMPOS DE DATOS DESDE empresa
    data = {
        "titulo": titulo, #"REPORTE MONITOREO",
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
        "CENAM": "CNAM",
        "CNAM": "CNAM",
    }
    paisComplete = pais_abrev.get(empresa.pais, empresa.pais)
    # CADENAS DE MESE PARA LAS CONSULTAS DE 5 MESES 
    cadena_mes  = ",".join(meses[f"MESN_{i}"] for i in range(5, 0, -1)) + "," + meses["MESN"]
    cadena_anio =  "2025,2026" #",".join([meses["ANO_1"], meses["ANO_2"]])
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
        "cadena_anio":cadena_anio,
        "total_enlaces": total_enlaces
    }

    #DATOS DE LOS HI HISTORICOS INDICADORES 
    hi_indi= obtener_historico_indicadores( conn, datosPag )
    hi_indi = normalizar_dinamico(hi_indi)

    #TRAEMOS LOS DATOS DE LA PAGINA 8  ParqueCnoc
    pag8 =  Comporta8 (  datosPag)
    pag8 = normalizar_dinamico(pag8)

    #ejem = obtener_comportamiento_sql(datosPag)
    #print(ejem)
    
    # FUNCION PARA OBTENER TODOS LOS DATOS DE LAS PAGINAS SELECCIONADAS 
    paginas_nombres = paginas["nombres"]
    paginas_data = generar_paginas_data(paginas_nombres, PAGINAS_CONFIG, datosPag, cadena_mes)

    # VAMOS A SEGMENTAR TODOS LOS VALORES DE LA ULTIMA CONSULTA Y QUEREMOS REALIZAR UNA PAGINACION DE DATOS 
    if "pag_21" in paginas_data:
        Disponibilidad = paginacion(paginas_data["pag_21"])
    else:
        Disponibilidad = []

    # SOLO PARA LA PAGINA 23 TAMBIEN QUIEREN ENVIAR VARIOS VALORES 
    if "pag_23" in paginas_data:
        # print("QUE PUTAS AQUI NO DEBE DE PASAR")
        ochoHoras = paginacion8(
            paginas_data["pag_23"]["rows"],
            filas_por_pagina=25
        )
    else:
        ochoHoras = []

    ## FALTA AGREGAR LA CANTIDAD DE SITIOS AGREGADO AL MODELO DE HISTORICO DONDE MES Y AÑO SEA IGUAL A 
    #************************************************************************************************************
    requeridos1 = ["CLIENTE", "CLARO"]
    requeridos2 = ["MONITOREO REACTIVO", "MONITOREO PROACTIVO"]
    
    # paginas_data que sume y genere los totales y lo agrege al rows y header de total PARA LA PAG 10 
    if 'pag_10' in paginas_data:
        validaROWS10(paginas_data['pag_10'], requeridos2 )

    if 'pag_11' in paginas_data:
        validaROWS10(paginas_data['pag_11'], requeridos1 )

    if 'pag_16' in paginas_data:
        validaROWS10(paginas_data['pag_16'], requeridos1 )

    if 'pag_5' in paginas_data:
        validaROWS10(paginas_data['pag_5'], requeridos1 )
      
    # ========================== 
    return render(
        request,
        "template_reporte/Mensuales.html",
        {
            "id": 1 ,
            "data": data,
            "meses": meses,     # CAL CULO DE LOS MESES 
            "hi_indi": hi_indi, # INIDISPENSABLE PARA LA PAG 7 
            # "sql": sql,
            # "empresa": empresa,
            "mes": nombre_mes,
            "anio": anio,   
            "paginas": paginas, # orden y listado de paginas  
            "paginas_data": paginas_data ,  # DATOS DE TODAS LAS PAGINAS PAG1, PAG2 ... PAG 21
            "Disponibilidad": Disponibilidad, # PAG 21
            "ochoHoras": ochoHoras,   # ENLACES DE RESOLUCIÓN MAYOR A 8 HORAS
            "pag8": pag8     # Comportamiento de la Red del Cliente
        }
    )

#http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=MARZO&anio=2026&total_enlaces=55