from django.urls import path, include
from rest_framework import routers
from .views import ListClientes

router = routers.DefaultRouter()

router.register(r'clientes', ListClientes)

urlpatterns = [
    path('', include(router.urls))
]
