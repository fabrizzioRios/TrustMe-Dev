from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from trustme_test.models import Opinion, Pagina, Rfc, Usuarios, Validacion


class OpinionSerializer(ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'


class PageSerializer(ModelSerializer):
    opinions = OpinionSerializer()
    class Meta:
        model = Pagina
        fields = '__all__'


class RfcSerializer(ModelSerializer):
    class Meta:
        model = Rfc
        fields = '__all__'


class UserSerializer(ModelSerializer):
    rfc = RfcSerializer()
    class Meta:
        model = Usuarios
        fields = '__all__'




class ValidationSerializer(ModelSerializer):
    class Meta:
        model = Validacion
        fields = '__all__'


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('correo', 'contraseña')
