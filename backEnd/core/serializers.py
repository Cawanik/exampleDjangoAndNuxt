from rest_framework import serializers
from .models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ("id", "first_name", "last_name", "patronymic", "age", "sex", "is_married", "role_id")
