from rest_framework import serializers

from modalities.models import Modality
from teachers.models import Teacher

from django.shortcuts import get_object_or_404

from users.serializers import GeneralUserSerializer


class TeachersSerializer(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:

        model = Teacher

        fields = "__all__"


class ModalitySerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer(read_only=True)
    teacher_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Modality

        fields = [
            "id",
            "name",
            "teacher",
            "teacher_id",
        ]

    def create(self, validated_data):
        teacher_id = validated_data.pop("teacher_id")

        teacher = get_object_or_404(Teacher, id=teacher_id)

        modality = Modality.objects.create(**validated_data, teacher=teacher)

        return modality
