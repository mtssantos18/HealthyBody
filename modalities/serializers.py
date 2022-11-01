from rest_framework import serializers

from modalities.models import Modality


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = [
            "id",
            "name",
            # "teachers",  Uncomment when teacher's model is done.
        ]
