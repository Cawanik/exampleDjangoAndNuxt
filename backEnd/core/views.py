from rest_framework import viewsets
from .serializers import HumanSerializer
from .models import Human
from .serializers import RoleSerializer
from .models import Role


class HumanViewSet(viewsets.ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

