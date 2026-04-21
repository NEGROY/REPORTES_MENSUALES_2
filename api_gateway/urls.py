from django.urls import path

from .views import *

#  CnocCronologiaApiView,     CnocHistorialDiarioApiView,     CnocBusquedaTkApiView,


app_name = 'api_gateway'

urlpatterns = [
    path(
        'cnoc/cronologia/',
        CnocCronologiaApiView.as_view(),
        name='cnoc_cronologia'
    ),

    path(
        'cnoc/historial-diario/',
        CnocHistorialDiarioApiView.as_view(),
        name='cnoc_historial_diario'
    ),


    path(
        'cnoc/busqueda-tk/<str:falla_id>/',
        CnocBusquedaTkApiView.as_view(),
        name='cnoc_busqueda_tk'
    ),

    
    path(
        'cnoc/ultimo_seguimeinto/',
        CnocUltimoSeguimientoApiView.as_view(),
        name='cnoc_ultimo_seguimeinto_legacy'
    ),

    
    path(
        'cnoc/tickets/',
        CnocTicketsApiView.as_view(),
        name='cnoc_tickets'
    ),


]