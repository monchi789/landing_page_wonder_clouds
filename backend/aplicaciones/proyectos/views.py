from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Proyectos
from .serializer import ProyectosSerializer

# Create your views here.
class ProyectosViewSet(viewsets.ViewSet):
    """
    Vista simple para listar proyectos.
    """
    def list(self, request):
        queryset = Proyectos.objects.all()
        serializer = ProyectosSerializer(queryset, many=True)
        return Response(serializer.data)
