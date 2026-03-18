from django.shortcuts import render
from app.models.pag_reporte import PagReporte

def reporteXcliente(request):

    reporte = PagReporte.objects.filter(estado=True).first()

    paginas = []
    templates_paginas = []

    if reporte:
        paginas = reporte.paginas
        templates_paginas = [f"paginas/pag{p}.html" for p in paginas]

    context = {
        "reporte": reporte,
        "paginas": paginas,
        "templates_paginas": templates_paginas
    }

    return render(request, "template_reporte/reporteXcliente.html", context)

