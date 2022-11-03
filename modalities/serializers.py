from rest_framework import serializers
from modalities.models import Modality
from teachers.serializer import TeachersSerializer


class ModalitySerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer()

    class Meta:
        model = Modality

        fields = [
            "id",
            "name",
            "teacher",
        ]
