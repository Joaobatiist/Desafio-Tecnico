from rest_framework.routers import DefaultRouter
from .views import TrilhaViewSet, EtapaViewSet

router = DefaultRouter()
router.register(r'trilhas', TrilhaViewSet)
router.register(r'etapas', EtapaViewSet)

urlpatterns = router.urls