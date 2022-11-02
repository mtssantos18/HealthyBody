from rest_framework.serializers import ModelSerializer, ValidationError

from customers.models import Customer
from users.models import User
from users.serializers import UserSerializer


class CustomerSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        validated_data["user"] = user

        customer = Customer.objects.create(**validated_data)
        return customer
