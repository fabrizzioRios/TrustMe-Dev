
from django.contrib import admin
from django.urls import path

from trustme_test.views import UserView, UserDetailView

urlpatterns = [
    path('user/', UserView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
