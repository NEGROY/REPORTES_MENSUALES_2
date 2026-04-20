from django.shortcuts import render
from cnoc_app.decorators import usuario_login_required


@usuario_login_required
def home_view(request):
    return render(request, 'home.html', {
        'usuario': request.user
    })

