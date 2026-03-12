from django.urls import path
# from .views.template_reporte.vista_prueba import vista_prueba_template ELIMINADAAA
from .views.template_reporte.reporteXcliente import reporteXcliente
from .views.template_reporte.presentacion_view import presentacion_original
    # IMPORT CORRECTO
from .views.menu.menu_views import menu
from .views.menu.infoCliente import infoCliente

urlpatterns = [
    path('reporteXcliente/', reporteXcliente, name='prueba_template'),
    # path('reporteXcliente/<int:id_cliente>/', reporteXcliente, name='prueba_template'), 
    path('reporteDEMO/', presentacion_original, name='DEMOS' ),
        # MENU PRINCIPAL
    path('', menu, name='menu'),
    path('infoCliente/', infoCliente, name='infoCliente'),
]