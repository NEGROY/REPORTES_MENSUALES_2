from cnoc_app.models import Usuario
from django.contrib.auth.backends import BaseBackend
import hashlib


class UsuarioBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # print("\n" + "=" * 80)                    # print("DEBUG LOGIN - INICIO AUTHENTICATE")
        # print(f"Username recibido: {username}")   # print(f"Password recibida: {'*' * len(password) if password else 'None'}")

        if not username or not password:
            # print("ERROR: username o password vienen vacíos")            # print("=" * 80 + "\n")
            return None

        try:
            usuario = Usuario.objects.get(
                username2=username,
                activo=True,
                baja=True
            )
            # print("\n--- DATOS RECUPERADOS DE BD ---")    # print(f"ID: {usuario.id}")
            # print(f"Username: {usuario.username2}")       # print(f"Email: {usuario.email}")
            # print(f"Activo: {usuario.activo}")            # print(f"Baja: {usuario.baja}")
            # print(f"IBM: {usuario.ibm}")                  # print(f"Agente: {usuario.agente}")
            # print(f"Teléfono: {usuario.telefono}")            # print(f"Hash en BD: {usuario.password_hash}")
            # print(f"Pass plain en BD: {usuario.pass_plain}")  # SOLO PARA DESARROLLO

            password_hash = hashlib.sha256(password.encode()).hexdigest()
            # print("\n--- COMPARACIÓN DE HASH ---") #print(f"Hash generado con input: {password_hash}") #print(f"Hash guardado en BD: {usuario.password_hash}") 
            # print(f"¿Coinciden?: {usuario.password_hash == password_hash}")

            if usuario.password_hash == password_hash:
               #print("RESULTADO: LOGIN CORRECTO")                #print("=" * 80 + "\n")
                return usuario

            #print("RESULTADO: LOGIN INVÁLIDO - HASH INCORRECTO") #print("=" * 80 + "\n")
            return None

        except Usuario.DoesNotExist:
            #print("RESULTADO: Usuario no existe o está inactivo / dado de baja") #print("=" * 80 + "\n")
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None