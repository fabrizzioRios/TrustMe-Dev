from trustme_test.models import Usuarios
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
