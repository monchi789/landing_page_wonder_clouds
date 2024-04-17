from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializer import ClienteSerializer
from .models import Cliente

# Create your views here.
class ListClientes(ListAPIView):
    get_queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
