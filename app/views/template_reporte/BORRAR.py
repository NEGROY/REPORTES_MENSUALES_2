from django.shortcuts import render
from datetime import datetime

from app.service.conexion import obtener_conexion
from app.service.reportes_sql import historico_de_indicadores
from app.service.funciones import ultimos_6_meses
from app.service.PAG_func import get_pag_General, get_pag_MesActual

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
    # -----------------------------

    # EMPRESA || SI ESTA VACIA QUE SEA 3 (PRUEBAS POR DEFAULT )
    if not id_empresa:
        id_empresa = 3
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
    # FECHA FORMATO 01012026
    # -----------------------------
    fechaINI = "01" + mes + anio
    # convertir 2026-01-01 -> 01012026 fechaINI = fechaINI.replace("-", "")
    
    # -----------------------------
    # OBTIENE LOS DATOS DE LA EMPRESA 
    # -----------------------------
    empresa = None
    if id_empresa:
        empresa = EmpresasCatalogo.objects.get(COD=id_empresa)

        # VALIDAR SI CAMBIO TOTAL ENLACES
        if total_enlaces:
            total_enlaces = int(total_enlaces)

            if empresa.tt_sitioa != total_enlaces:
                empresa.tt_sitioa = total_enlaces
                empresa.save(update_fields=["tt_sitioa"])

    # CONSULTA ORACLE
    conn = obtener_conexion()
    cursor = conn.cursor()

    # REALZIA CONSULTA DE LOS DATOS DE historico_de_indicadores  
    if empresa:
        sql = historico_de_indicadores(empresa.parque_where)
        # sql = historico_de_indicadores()
    else:
        sql = historico_de_indicadores()
 
    cursor.execute(sql)
    columnas = [col[0] for col in cursor.description]
    resultados = []
    for fila in cursor.fetchall():
        resultados.append(dict(zip(columnas, fila)))
    #CIERRA LAS CONEXIONES cursor.close() conn.close()
    cursor.close() 
    conn.close()

    # FUNCION PARA CALCULAR LOS ULTIMOS 6 MESES 
    meses = ultimos_6_meses(int(mes), int(anio))

    # CASE DE PAIS ABREVISATURAS 
    pais_abrev = {
        "GT": "GUATEMALA",
        "SV": "EL SALVADOR",
        "HN": "HONDURAS",
        "NI": "NICARAGUA",
        "CR": "COSTA RICA",
        "CENAM": "CENAM"
    }
    paisComplete = pais_abrev.get(empresa.pais, empresa.pais)

    # EMPEZAMOS A CREAR LOS DATOS PARA LAS PAGINAS 
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

    # pagina de cadena_mes
    cadena_mes = ",".join(meses[f"MESN_{i}"] for i in range(5, 0, -1)) + "," + meses["MESN"]
    # func_sql VARIABLES PARA MI FUNCION GENERAL DE  get_pag_General
    func_sql =  "pag_5"  # ||pag_20

    # ==========================
    # DATOS PARA PAGINA 7
    # pag11 = get_pag_General(datosPag, cadena_mes, func_sql)
    pag11 = get_pag_MesActual(datosPag, func_sql)

    # ========================== EJEMPLO    # DATOS PARA PAGINA 5    # pag5 = get_pag5(datosp5)

    return render(
        request,
        "template_reporte/preuba.html",
        {
            "id": pag11 ,
            "data": resultados,
            "meses": meses,
            "sql": sql,
            "empresa": empresa,
            "mes": mes,
            "anio": anio
        }
    )

#http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=MARZO&anio=2026&total_enlaces=55