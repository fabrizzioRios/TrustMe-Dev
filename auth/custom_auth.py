from django.contrib.auth.backends import ModelBackend
from rest_framework.generics import get_object_or_404

from trustme_test.models import Usuarios


class CustomAuthBackend():
    @classmethod
    def authenticate(cls, correo, contraseña):
        try:

            user = Usuarios.objects.get(correo=correo, contraseña=contraseña)
            return user
        except Usuarios.DoesNotExist:
            return {"id_usuario": -1, "correo": None, "contraseña": None}

