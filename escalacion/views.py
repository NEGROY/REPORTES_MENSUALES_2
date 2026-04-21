from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

# para lOS MODELOS 
from cnoc_app.models import Pais  # importar el modelo
from .models import EscalacionArea
# from .service import listar_areasXpais
# PARA REUTILIZAR LOS SELECT DE LOS MODELOS YA HECHOS
from .service.factory import SelectServiceFactory


# TABLARO DE ESCALACION SOLO FRONT END 
    # DE LAS FALAS ESCALADAS, SI EL USUARIO ES del AREA DE LIDER, SE DEBE DE TENER UN FILTRO PARA QUE SE MUESTREN EL DE LA AREA CORRESPONDIENTE 
    # RECUERDA que la FALLAS DE *NOCTURNO* deben de ser escaladas BAJO EL ID 12 para MUETSREN (soc, reactivo, WO, PROACTIVO,)
    # ADEMAS AGREGAR QUE SE RECARGUE CADA 1 MIN, ( ademas de validar si cada falla abierta ya paso del tiempo o si ya se ecnuentra cerrado  )
def tablero_escalacion(request):
    return render(request, 'escalacion/tablero.html' )

# FALLAS ASOCIADAS A LAS MASIVAS 
    # SE INGRESA UNA FALLA MASIVA SE VALIDA SI SE ENCUNTRA ABIERTA 
    # SE MUESTYRAN TODAS LAS FALLAS MASIVAS QUE SE TIENEN ASOVCIADAS 
    # QUE SE ALMACENEN LOS DATOS DE VRF, WAN, etc 
    # se puede exportar a EXCEL LOS DATOS DE TODAS LAS QUE SE HAN GUARDADO 
def fallas_asociadas(request):
    return render(request, 'escalacion/fallas_asociadas.html')


# ********************************************************************
# PRUEBA DE REFACTORIZACION Y POLYMORFISMO
def api_areas_por_pais(request, pais_id):
    service = SelectServiceFactory.build('areas_por_pais', pais_id=pais_id)
    data = service.execute()

    return JsonResponse({
        'ok': True,
        'data': data,
    })

def tablas_escalacion(request):
    service = SelectServiceFactory.build('paises')
    paises = service.execute()

    return render(request, 'escalacion/tablas_escalacion.html', {
        'paises': paises,
    })
# ********************************************************************


#

#

#

