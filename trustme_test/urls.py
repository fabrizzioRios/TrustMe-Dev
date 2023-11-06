
from django.urls import path, include

from .views.login_view import LoginView

from .routers import router

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api/v1/', include(router.urls)),
]
