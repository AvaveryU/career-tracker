from django.urls import include, path

from rest_framework import routers

from .views import StudentUserViewSet


app_name = "api"

# Роутер для API версии 1
router_v1 = routers.DefaultRouter()
router_v1.register(r"test", StudentUserViewSet, "users")

urlpatterns = (
    path("", include(router_v1.urls)),
    path("auth/", include("djoser.urls")),
)
