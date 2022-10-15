from rest_framework import serializers
from .models import Human
from .models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "name")


class HumanSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Human
        fields = ["id", "first_name", "last_name", "patronymic", "age", "sex", "is_married", "email", "role"]
        extra_kwargs = {
            'role': {'write_only': True}
        }
