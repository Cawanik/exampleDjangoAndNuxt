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

    if int(request_data['age']) < 0:
        err.append({'age': ['Age cant contain digit below zero']})
    if not serializer.is_valid():
        print(serializer.errors)
        err.append('Serializers errors')

    return err


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

    def list(self, request, *args):
        all_fields = {'humans': HumanSerializer(Human.objects.all(), many=True).data,
                      'roles': RoleSerializer(Role.objects.all(), many=True).data,
                      'deleted': DeletedSerializer(Deleted.objects.all(), many=True).data}
        return Response(all_fields, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        errors = check_errors(request.data)
        if not errors:
            self.serializer_class = HumanAddSerializer
            return viewsets.ModelViewSet.create(self, request)
        else:
            print('Has error!', errors)
            return Response(errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def update(self, request, *args, **kwargs):
        errors = check_errors(request.data)
        if not errors:
            self.serializer_class = HumanAddSerializer
            return viewsets.ModelViewSet.update(self, request)
        else:
            print('Has error!', errors)
            return Response(errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

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
