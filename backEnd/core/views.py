from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from django.utils.timezone import make_aware


def check_errors(request_data):
    err = []
    serializer = HumanAddSerializer(data=request_data)
    if request_data['first_name'].isdigit() \
            or request_data['last_name'].isdigit() \
            or request_data['patronymic'].isdigit():
        err.append('Name cant contain digit')
    if not serializer.is_valid():
        err.append('Serializers errors')

    return err


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

    def create(self, request, *args, **kwargs):
        errors = check_errors(request.data)
        if not errors:
            self.serializer_class = HumanAddSerializer
            return viewsets.ModelViewSet.create(self, request)
        else:
            print('Has error!', errors)
            return Response(','.join(errors), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        errors = check_errors(request.data)
        if not errors:
            self.serializer_class = HumanAddSerializer
            return viewsets.ModelViewSet.update(self, request)
        else:
            print('Has error!', errors)
            return Response(','.join(errors), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        on_delete = self.get_object()
        Deleted.objects.create(
            first_name=on_delete.first_name,
            last_name=on_delete.last_name,
            patronymic=on_delete.patronymic,
            age=on_delete.age,
            sex=on_delete.sex,
            is_married=on_delete.is_married,
            role=on_delete.role,
            password=on_delete.password,
            email=on_delete.email,
        ).save()
        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class DeletedViewSet(viewsets.ModelViewSet):
    serializer_class = DeletedSerializer
    queryset = Deleted.objects.all()

    def destroy(self, request, *args, **kwargs):
        on_return = self.get_object()
        Human.objects.create(
            first_name=on_return.first_name,
            last_name=on_return.last_name,
            patronymic=on_return.patronymic,
            age=on_return.age,
            sex=on_return.sex,
            is_married=on_return.is_married,
            role=on_return.role,
            password=on_return.password,
            email=on_return.email,
        ).save()

        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)
