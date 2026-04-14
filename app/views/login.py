from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("\n" + "-" * 80)        # print("DEBUG VIEW LOGIN")
        # print(f"POST username: {username}")        # print(f"POST password: {'*' * len(password) if password else 'None'}")

        user = authenticate(request, username=username, password=password)

        print(f"Resultado authenticate(): {user}")
        print("-" * 80 + "\n")

        if user:
            # ✅ Sesión manual
            request.session['usuario_id'] = user.id
            request.session['username2'] = user.username2
            request.session['email'] = user.email
            request.session['agente'] = user.agente
            request.session['ibm'] = user.ibm
            request.session['area_id'] = user.area_id if user.area else None

            print(f"Usuario autenticado correctamente: {user.username2}")
            return redirect('home')
        else:
            print("Credenciales incorrectas")
            messages.error(request, 'Credenciales incorrectas')

    return render(request, 'login.html')