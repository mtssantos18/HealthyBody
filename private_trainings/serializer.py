from rest_framework import serializers
from .models import Private_training

from personals.serializers import PersonalAllSerializer

class PrivateSerializer(serializers.ModelSerializer):
    # customer_id = CustomerSerializer(read_only=True)
    # personal_id = PersonalAllSerializer(read_only=True)
    class Meta:
        model = Private_training
        fields = [
            "id",
            "date",
            "hour",
            "update_at",
            # "customer_id",
            # "personal_id"       
            ]