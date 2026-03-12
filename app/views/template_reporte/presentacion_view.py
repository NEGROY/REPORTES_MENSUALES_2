from django.shortcuts import render

def presentacion_original(request):

    data = {
        "titulo": "REPORTE MONITOREO",
        "nombre": "CLIENTE DEMO",
        "mes": "marzo",
        "anio": "2026",
        "sitios": 50,
        "nombre": 'BANCO DE LOS TRABAJADORES',
    }

    return render(
        request,
        "template_reporte/presentacion_original.html",
        {"data":data}
    )