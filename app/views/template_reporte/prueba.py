from django.shortcuts import render
from app.service.conexion import obtener_conexion
from app.service.reportes_sql import historico_de_indicadores
from app.service.funciones import ultimos_6_meses
from app.models.empresas_catalogo import EmpresasCatalogo

# http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=03&anio=2026&total_enlaces=55
def reporte_prueba(request):

    # PARAMETROS
    id_empresa = request.GET.get("empresa")
    mes = request.GET.get("mes")        # MARZO, ENERO, FEBREO
    anio = request.GET.get("anio")
    total_enlaces = request.GET.get("total_enlaces")

    # convertir 2026-01-01 -> 01012026 fechaINI = fechaINI.replace("-", "")

    empresa = None
    fechaINI = '0102' + anio

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

    meses = ultimos_6_meses(int(mes), int(anio))


    return render(
        request,
        "template_reporte/preuba.html",
        {
            "data": resultados,
            "meses": meses,
            "sql": sql,
            "id": id_empresa,
            "empresa": empresa,
            "mes": mes,
            "anio": anio
        }
    )

#http://127.0.0.1:8000/reporte-prueba/?empresa=3&mes=MARZO&anio=2026&total_enlaces=55