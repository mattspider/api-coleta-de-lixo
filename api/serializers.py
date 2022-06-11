from rest_framework import serializers

from api.models import Infanunciante, Infempresa, anuncios


class InfanunciantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infanunciante
        fields = '__all__'
class anunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = anuncios
        fields = '__all__'

class InfempresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infempresa
        fields = '__all__'


