from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "name")


class HumanAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"


class HumanSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Human
        fields = ["id", "first_name", "last_name", "patronymic", "age", "sex", "is_married", "role"]


class DeletedSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Deleted
        fields = ["id", "first_name", "last_name", "patronymic", "age", "sex", "is_married", "role"]


class AllSerializers(serializers.ModelSerializer):
    Human = HumanSerializer(read_only=True)
    Role = RoleSerializer(read_only=True)
    Deleted = DeletedSerializer(read_only=True)

    class Meta:
        fields = ['Human', 'Role', 'Deleted']
