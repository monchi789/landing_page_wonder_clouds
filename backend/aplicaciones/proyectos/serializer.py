from rest_framework import serializers
from .models import Proyectos

# Create the serializer here
class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('__all__')
