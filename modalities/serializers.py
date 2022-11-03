from rest_framework import serializers

from modalities.models import Modality
from teachers.models import Teacher

from users.serializers import GeneralUserSerializer


class TeachersSerializer(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:

        model = Teacher

        fields = "__all__"


class ModalitySerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer()

    class Meta:
        model = Modality

        fields = [
            "id",
            "name",
            "teacher",
        ]
