from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from api.models import Infanunciante, Infempresa, anuncios
from api.serializers import (InfanunciantesSerializer, InfempresaSerializer,
                              anunciosSerializer)

from rest_framework.filters import SearchFilter


class InfanuncianteViewSet(viewsets.ModelViewSet):
    queryset = Infanunciante.objects.all()
    serializer_class =InfanunciantesSerializer

    
    
class anunciosViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter,)
    search_fields = ['tipo']
    queryset = anuncios.objects.all()
    serializer_class = anunciosSerializer




class InfempresaViewSet(viewsets.ModelViewSet):
    queryset = Infempresa.objects.all()
    serializer_class = InfempresaSerializer

