from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializer import ClienteSerializer, ProyectosSerializer
from .models import Cliente, Proyectos

# Create your views here.
class ViewSetClientes(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ViewSetProyectos(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer
