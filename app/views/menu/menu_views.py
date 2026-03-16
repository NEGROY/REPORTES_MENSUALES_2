from django.shortcuts import render
from datetime import datetime
from app.models.empresas_catalogo import EmpresasCatalogo

def menu(request, pais=None):
    # FECHA ACTUAL
    hoy = datetime.now()
    meses = { 
        1: "ENERO",     2: "FEBRERO",   3: "MARZO",
        4:  "ABRIL",    5: "MAYO",      6: "JUNIO",
        7:  "JULIO",    8: "AGOSTO",    9: "SEPTIEMBRE",
        10: "OCTUBRE", 11: "NOVIEMBRE", 12: "DICIEMBRE"
    }
    mes = meses[hoy.month]
    anio = hoy.year
    #

    # EMPRESAS ACTIVAS
    empresas = EmpresasCatalogo.objects.filter(STATUS=1,pais=pais).order_by("ORDEN")
    # TOTAL DE SITIOS REGISTRADOS     # tt_sitioa
    
    data = {
        "mes_actual": mes,
        "anio_actual": anio,
        "empresas": empresas,
        "pais": pais
    }

    return render(request, "menu/menu.html", data)