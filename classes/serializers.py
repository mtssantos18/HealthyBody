from rest_framework import serializers

from classes.models import Class
from modalities.models import Modality
from teachers.models import Teacher
from users.serializers import GeneralUserSerializer
from django.shortcuts import get_object_or_404


class ClassModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = [
            "id",
            "name",
        ]
        read_only_fields = [
            "name",
        ]


class ClassTeachersSerializer(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:

        model = Teacher

        fields = [
            "user",
        ]


class PostClassSerializer(serializers.ModelSerializer):
    teacher = ClassTeachersSerializer(read_only=True)
    modality = ClassModalitySerializer(read_only=True)
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
    teacher = ClassTeachersSerializer(read_only=True)
    modality = ClassModalitySerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"
