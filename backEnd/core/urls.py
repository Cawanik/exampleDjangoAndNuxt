from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'humans', HumanViewSet)
router.register(r'role', RoleViewSet)
router.register(r'deleted', DeletedViewSet)
urlpatterns = [
    path("", include(router.urls))
]
