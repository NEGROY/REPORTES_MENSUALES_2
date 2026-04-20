from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

# para lOS MODELOS 
from cnoc_app.models import Pais  # importar el modelo
from .models import EscalacionArea
from .service import listar_areasXpais

# Create your views here.
# PASO 1 CREAR MI VISTA DEL TEMPLATE -> creAR EN EL URL 
def tablas_escalacion(request):
    #paises = Pais.objects.all().values('id', 'nombre_pais')
    paises = (
        Pais.objects
        .filter(id__gt=1)          # id mayor a 1
        .order_by('id')            # ordenado por id ascendente
        .values('id', 'nombre_pais')
    )
    context = {
        'paises': paises,
    }
    return render(request, 'escalacion/tablas_escalacion.html', context)

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

# DEFINIMOS para listar las areas de escalacion 
@require_GET
def api_areas_por_pais(request, pais_id):
    areas = (
        EscalacionArea.objects
        .filter(pais_id=pais_id, activo=True)
        .order_by('nombre_area')
        .values('id', 'nombre_area')
    )
    # PRUEBAS DE DATOS IMPRIMIDOS 
    data = list(areas)
    print(f'>>> Áreas encontradas: {data}')

    return JsonResponse({
        'ok': True,
        'data': list(areas)
    })

#

#