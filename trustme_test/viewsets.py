
from rest_framework import viewsets
from .models import User, Page, Opinion
from .serializer import UserSerializer, PageSerializer, OpinionSerializer, LoginResponseSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PageViewSets(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class OpinionViewSets(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class LoginViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginResponseSerializer
