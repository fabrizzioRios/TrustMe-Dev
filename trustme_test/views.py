from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from trustme_test.models import User
from trustme_test.serializer import UserSerializer


class UserView(APIView):
    def get(self, request):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)

    def post(self, request, pk):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            account = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = User.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
