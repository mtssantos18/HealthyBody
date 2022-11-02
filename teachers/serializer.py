from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from teachers.models import Teacher
from users.models import User
from users.serializers import UserSerializer


class TeachersSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:

        model = Teacher

        fields = "__all__"

        # exclude = ["id"]

    def create(self, validated_data: dict):

        request_user = validated_data.pop("user")

        user = User.objects.create_user(**request_user)

        return Teacher.objects.create(user=user)
