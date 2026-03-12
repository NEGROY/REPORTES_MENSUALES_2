from django.shortcuts import render
from app.models.empresas_catalogo import EmpresasCatalogo

def infoCliente(request):
    id_empresa = request.GET.get("empresa")
    total_enlaces = request.GET.get("total_enlaces")
    empresa = None

    if id_empresa:
        # CONSULTAR EMPRESA
        empresa = EmpresasCatalogo.objects.get(COD=id_empresa)
        # VALIDAR SI CAMBIO EL TOTAL DE ENLACES
        if total_enlaces:
            total_enlaces = int(total_enlaces)
            if empresa.tt_sitioa != total_enlaces:
                # ACTUALIZAR VALOR
                empresa.tt_sitioa = total_enlaces
                empresa.save(update_fields=["tt_sitioa"])

    data = {
        "empresa": empresa
    }

    return render(request, "menu/infoCliente.html", data)