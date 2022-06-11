from django.urls import include, path
from rest_framework import routers

from api.views import (InfanuncianteViewSet, InfempresaViewSet,
                       anunciosViewSet)

router = routers.DefaultRouter()

router.register(r'infanunciante', InfanuncianteViewSet)
router.register(r'anuncio', anunciosViewSet)
router.register(r'infempresas', InfempresaViewSet)


urlpatterns = [
    path("", include(router.urls)),
]