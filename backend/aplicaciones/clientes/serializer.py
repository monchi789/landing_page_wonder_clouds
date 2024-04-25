from rest_framework import serializers
from .models import Cliente, Proyectos

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')


class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('__all__')
