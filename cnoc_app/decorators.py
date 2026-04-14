from django.shortcuts import redirect


def usuario_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user or not hasattr(request.user, 'username2'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper