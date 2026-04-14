from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user, backend='cnoc_app.auth_backend.UsuarioBackend')
            return redirect('/cnoc/escalacion/')
        else:
            messages.error(request, "Credenciales incorrectas")

    return render(request, 'login.html')