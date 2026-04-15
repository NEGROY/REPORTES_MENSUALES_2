from django.shortcuts import render

# Create your views here.
#PASO 1 CREAR MI VISTA DEL TEMPLATE

def tablas_escalacion(request):
    context = {
        'paises': [],
    }
    return render(request, 'escalacion/tablas_escalacion.html', context)

