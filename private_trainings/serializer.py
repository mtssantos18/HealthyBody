from rest_framework import serializers
from .models import Private_training

from personals.serializers import PersonalAllSerializer

class PrivateSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)
    personal = PersonalAllSerializer(read_only=True)
    class Meta:
        model = Private_training
        fields = [
            "id",
            "date",
            "hour",
            "update_at",
            "personal"       
            ]