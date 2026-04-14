from django.urls import path
# from .views.template_reporte.vista_prueba import vista_prueba_template ELIMINADAAA
from .views.template_reporte.reporteXcliente import reporteXcliente
from .views.template_reporte.presentacion_view import presentacion_original
    # IMPORT CORRECTO
from .views.menu.menu_views import menu
from .views.menu.infoCliente import infoCliente
    # IMPORT DE LAS  PRUEBAS 
from app.views.template_reporte.prueba import reporte_prueba
from app.views.login import login_view
from app.views.home import home_view



urlpatterns = [
    path('reporteXcliente/', reporteXcliente, name='prueba_template'),
    # path('reporteXcliente/<int:id_cliente>/', reporteXcliente, name='prueba_template'), 
    path('reporteDEMO/', presentacion_original, name='DEMOS' ),
        # MENU PRINCIPAL
    path("menu/<str:pais>/", menu, name="menu_pais"),  #path('', menu, name='menu'), #/<str:pais>/
    path('infoCliente/', infoCliente, name='infoCliente'),
    # para mis pruebas LOCAS
    path('reporte-prueba/', reporte_prueba, name='reporte_prueba'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),

]