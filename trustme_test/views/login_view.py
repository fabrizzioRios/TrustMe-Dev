
from django.contrib.auth import authenticate, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from trustme_test.models import User
from trustme_test.serializer import LoginSerializer, LoginResponseSerializer


class LoginView(APIView):
    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            raise Exception(login_serializer.errors)
        try:
            logout(request)
            email = login_serializer.data.get('email')
            password = login_serializer.data.get('password')
            user = User.objects.filter(email=email).first()
            if not user:
                raise Exception("This user doesn't exists")
            authenticate(username=email, password=password)
            result = LoginResponseSerializer(user).data
        except Exception as err:
            return Response({
                "success": False,
                "message": f"{err}"
            },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({
            "success": True,
            "message": result
        }, status.HTTP_200_OK)
