from rest_framework import serializers

from classes.models import Class
from modalities.models import Modality
from teachers.models import Teacher
from users.models import User

from django.shortcuts import get_object_or_404


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = [
            "id",
            "name",
        ]
        read_only_fields = [
            "name",
        ]


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "phone",
        ]

    def get_full_name(self, obj) -> str:
        return obj.obtain_full_name()


class TeachersSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:

        model = Teacher

        fields = [
            "user",
        ]


class PostClassSerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer(read_only=True)
    modality = ModalitySerializer(read_only=True)
    modality_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Class
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "hour": {"required": True},
            "duration": {"required": True},
            "capacity": {"required": True},
        }

    def create(self, validated_data):
        check_modality = validated_data.pop("modality_id")
        modality_found = get_object_or_404(Modality, id=check_modality)

        new_class = Class.objects.create(**validated_data, modality=modality_found)

        return new_class


class ListClassSerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer(read_only=True)
    modality = ModalitySerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"
