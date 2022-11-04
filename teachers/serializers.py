from rest_framework import serializers
from teachers.models import Teacher
from modalities.models import Modality
from users.models import User
from users.serializers import UserSerializer


class TeacherModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = [
            "id",
            "name",
        ]


class TeachersSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    modalities = TeacherModalitySerializer(many=True, read_only=True)

    class Meta:

        model = Teacher

        fields = ["id", "user", "modalities"]

        depth = 1

    def create(self, validated_data: dict):

        request_user = validated_data.pop("user")

        user = User.objects.create_user(**request_user)

        return Teacher.objects.create(user=user)

    def update(self, instance: Teacher, validated_data):

        request_user = validated_data.pop("user")

        for key, value in request_user.items():
            setattr(instance.user, key, value)

        instance.user.save()

        return instance
