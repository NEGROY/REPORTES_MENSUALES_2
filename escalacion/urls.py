from django.urls import path
from . import views

app_name = 'escalacion'

urlpatterns = [
    path('', views.tablas_escalacion, name='tableroEscalacion'),
]