from django.urls import path, include
from rest_framework import routers
from .views import ViewSetClientes, ViewSetProyectos

router = routers.DefaultRouter()

router.register(r'clientes', ViewSetClientes, 'Clientes')
router.register(r'proyectos', ViewSetProyectos, 'Proyectos')

urlpatterns = [
    path('', include(router.urls))
]
