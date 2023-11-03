
from django.urls import path

from trustme_test.views import LoginView, UserView, UserDetailView, PageView, PageDetailView, OpinionView, \
    OpinionViewDetail, ValidationView, ValidationDetailView, RfcView, RfcDetailView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('users/', UserView.as_view(), name='user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('validations/', ValidationView.as_view(), name='validations'),
    path('validations/<int_pk>/', ValidationDetailView.as_view(), name='validation-detail'),

    path('pages/', PageView.as_view(), name="pages"),
    path('pages/<int:pk>/', PageDetailView.as_view(), name="page-detail"),

    path('opinions/', OpinionView.as_view(), name="opinions"),
    path('opinions/<int:pk>/', OpinionViewDetail.as_view(), name="opinion-detail"),

    path('rfcs/', RfcView.as_view(), name='rfc'),
    path('rfcs/<str:rfc_complete>', RfcDetailView.as_view(), name='rfc-detail'),
]
