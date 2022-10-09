from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HumanViewSet
from .views import RoleViewSet

router = DefaultRouter()
router.register(r'humans', HumanViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = [
    path("", include(router.urls))
]
