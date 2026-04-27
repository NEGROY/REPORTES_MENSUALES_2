from django.urls import path
from . import views

app_name = 'escalacion'

# PASO 2 crear url -> validar URL EN CONFIG/URLS 
urlpatterns = [
    path('', views.tablas_escalacion, name='tableroEscalacion'),
    path('tablero', views.tablero_escalacion, name='tablero'),
    path('Asociadas', views.fallas_asociadas, name='fallas_asociadas'), 

    # APIS 
    path('api/paises/<int:pais_id>/areas/', views.api_areas_por_pais, name='api_areas_por_pais'),

    # rutas locas
    path('api/calculadora/', views.api_tabla_calculadora, name='api_tabla_calculadora'),
]