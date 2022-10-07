from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HumanViewSet

router = DefaultRouter()
router.register(r'humans', HumanViewSet)

urlpatterns = [
    path("", include(router.urls))
]
