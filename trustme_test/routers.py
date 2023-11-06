
from rest_framework import routers
from .viewsets import UserViewSets, PageViewSets, OpinionViewSets, LoginViewSets

router = routers.DefaultRouter()
router.register(
    "users",
    UserViewSets,
    basename='users_viewsets'
)
router.register(
    "pages",
    PageViewSets,
    basename='pages_viewsets'
)
router.register(
    "opinions",
    OpinionViewSets,
    basename='opinions_viewsets'
)
router.register(
    "login",
    LoginViewSets,
    basename='login_viewsets'
)

