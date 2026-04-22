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


# APIS DE MASIVAS 
    path(
        'masivas/tiempos/',
        MasivasTiempoApiView.as_view(),
        name='masivas_tiempos'
    ),

    path(
        'masivas/MasivasTiempo/',
        MasivasTiempoApiView.as_view(),
        name='masivas_tiempos_legacy'
    ),


    path(
        'masivas/fallas-masivas/<str:fallas>/',
        FallasMasivasApiView.as_view(),
        name='fallas_masivas'
    ),


    path(
        'masivas/clocks/<str:falla>/',
        ClocksFallaApiView.as_view(),
        name='clocks_falla'
    ),
   

    path(
        'masivas/list/<str:id>/',
        MasivasListApiView.as_view(),
        name='masivas_list'
    ),


    path(
        'masivas/<str:id>/',
        MasivaDetalleApiView.as_view(),
        name='masiva_detalle'
    ),


    path(
        'masivas/',
        MasivasApiView.as_view(),
        name='masivas'
    ),


]