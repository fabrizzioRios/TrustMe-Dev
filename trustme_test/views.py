from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from trustme_test.models import Opinion, Pagina, Rfc, Usuarios
from trustme_test.serializer import LoginSerializer, OpinionSerializer, PageSerializer, UserSerializer, RfcSerializer
from auth.custom_auth import CustomAuthBackend

""" Login view - functional but with no implementation at the moment """


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['correo']
            password = serializer.validated_data['contraseña']
            # user = authenticate(request, username=email, password=password)
            auth = CustomAuthBackend()
            user = auth.authenticate(self, email, password)
            print(user)
            if user is not None:
                print(login(request, user=user))
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" Opinion views """


class OpinionView(APIView):
    def get(self, request):
        opinion = Opinion.objects.all()
        opinion_serializer = PageSerializer(opinion, many=True)
        return Response(opinion_serializer.data)

    def post(self, request):
        opinion_serializer = OpinionSerializer(data=request.data)

        if opinion_serializer.is_valid():
            opinion_serializer.save()
            return Response(opinion_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(opinion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpinionViewDetail(APIView):
    def get(self, request, pk):
        try:
            opinion = Opinion.objects.get(pk=pk)
        except Opinion.DoesNotExist:
            return Response({'Error': 'Opinion not found'}, status=status.HTTP_404_NOT_FOUND)

        opinion_serializer = OpinionSerializer(opinion)
        return Response(opinion_serializer.data)

    def put(self, request, pk):
        opinion = Pagina.objects.get(pk=pk)
        opinion_serializer = OpinionSerializer(opinion, data=request.data)
        if opinion_serializer.is_valid():
            opinion_serializer.save()
            return Response(opinion_serializer.data)
        else:
            return Response(opinion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        opinion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" Page related view"""


class PageView(APIView):
    def get(self, request):
        page = Pagina.objects.all()
        page_serializer = PageSerializer(page, many=True)
        return Response(page_serializer.data)

    def post(self, request):
        page_serializer = UserSerializer(data=request.data)

        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetailView(APIView):
    def get(self, request, pk):
        try:
            page = Pagina.objects.get(pk=pk)
        except Pagina.DoesNotExist:
            return Response({'Error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        page_serializer = PageSerializer(page)
        return Response(page_serializer.data)

    def put(self, request, pk):
        page = Pagina.objects.get(pk=pk)
        page_serializer = PageSerializer(page, data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data)
        else:
            return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        page = Pagina.objects.get(pk=pk)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" Page related view"""


class ValidationView(APIView):
    def get(self, request):
        page = Pagina.objects.all()
        page_serializer = PageSerializer(page, many=True)
        return Response(page_serializer.data)

    def post(self, request):
        page_serializer = UserSerializer(data=request.data)

        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidationDetailView(APIView):
    def get(self, request, pk):
        try:
            page = Pagina.objects.get(pk=pk)
        except Pagina.DoesNotExist:
            return Response({'Error': 'Validation not found'}, status=status.HTTP_404_NOT_FOUND)

        page_serializer = PageSerializer(page)
        return Response(page_serializer.data)

    def put(self, request, pk):
        page = Pagina.objects.get(pk=pk)
        page_serializer = PageSerializer(page, data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data)
        else:
            return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        page = Pagina.objects.get(pk=pk)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""" User related views """


class RfcView(APIView):
    def get(self, request):
        rfc = Rfc.objects.all()
        rfc_serializer = RfcSerializer(rfc, many=True)
        return Response(rfc_serializer.data)

    def post(self, request):
        rfc_serializer = RfcSerializer(data=request.data)

        if rfc_serializer.is_valid():
            rfc_serializer.save()
            return Response(rfc_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(rfc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RfcDetailView(APIView):
    def get(self, request, pk):
        try:
            rfc = Rfc.objects.get(pk=pk)
        except Rfc.DoesNotExist:
            return Response({'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(rfc)
        return Response(serializer.data)

    def put(self, request, pk):
        rfc = Usuarios.objects.get(pk=pk)
        rfc_serializer = RfcSerializer(rfc, data=request.data)
        if rfc_serializer.is_valid():
            rfc_serializer.save()
            return Response(rfc_serializer.data)
        else:
            return Response(rfc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rfc = Rfc.objects.get(pk=pk)
        rfc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" User related views """


class UserView(APIView):
    def get(self, request):
        user = Usuarios.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            account = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response({'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk):
        user = Usuarios.objects.get(pk=pk)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = Usuarios.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""""""
