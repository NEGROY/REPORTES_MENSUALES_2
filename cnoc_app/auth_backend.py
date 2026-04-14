from cnoc_app.models import Usuario
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.hashers import check_password

import hashlib


class UsuarioBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            usuario = Usuario.objects.get(
                username2=username,
                activo=True,
                baja=False
            )

            # 🔐 Validación estilo PHP (ejemplo SHA256 / MD5)
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if usuario.password_hash == password_hash:
                return usuario

        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None