from django.shortcuts import render
# para el admin y el HOME 
from django.http import HttpResponse
from cnoc_app.decorators import usuario_login_required



# Create your views here.

@usuario_login_required
def tablas_escalacion_view(request):
    return HttpResponse("Módulo: Tablas de Escalación")

@usuario_login_required
def asientos_view(request):
    return HttpResponse("Módulo: Asignación de Asientos")

@usuario_login_required
def retroalimentacion_view(request):
    return HttpResponse("Módulo: Retroalimentación")
