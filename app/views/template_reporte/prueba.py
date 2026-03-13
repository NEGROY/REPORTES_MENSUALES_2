from django.shortcuts import render
from app.service.conexion import obtener_conexion
from app.service.reportes_sql import historico_de_indicadores
# datos del modelo 
from app.models.empresas_catalogo import EmpresasCatalogo


def reporte_prueba(request):
    # CONSULTA ORACLE
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = historico_de_indicadores()
    ##sql = historico_de_indicadores(empresa.parque_where)
    cursor.execute(sql)

    columnas = [col[0] for col in cursor.description]

    resultados = []
    for fila in cursor.fetchall():
        resultados.append(dict(zip(columnas, fila)))

    cursor.close()
    conn.close()

    # CONSULTA DJANGO ORM
    empresas = EmpresasCatalogo.objects.filter(COD=2).order_by("ORDEN")

    return render(
        request,
        "template_reporte/preuba.html",
        {
            "data": resultados,
            "empresas": empresas
        }
    )