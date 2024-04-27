from rest_framework.routers import DefaultRouter
from .views import ProyectosViewSet

router = DefaultRouter()

router.register(r'proyectos', ProyectosViewSet, basename='proyecto')

urlpatterns = router.urls
