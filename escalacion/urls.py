from django.urls import path
from . import views

app_name = 'escalacion'

# PASO 2 crear url -> validar URL EN CONFIG/URLS 

urlpatterns = [
    path('', views.tablas_escalacion, name='tableroEscalacion'),
    path('tablero', views.tablero_escalacion, name='tablero'),
    path('Asociadas', views.fallas_asociadas, name='fallas_asociadas'), 
]