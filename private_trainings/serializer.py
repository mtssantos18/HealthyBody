from rest_framework import serializers
from .models import Private_training
from personals.models import Personal
from customers.models import Customer

from django.shortcuts import get_object_or_404

from users.models import User


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


class PersonalSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Personal
        fields = [
            "id",
            "user",
            "check_in",
            "check_out",
        ]
        read_only_fields = ["check_in", "check_out"]


class CustomerSerializerPT(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:

        model = Customer

        fields = [
            "user",
        ]


class PrivateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializerPT(read_only=True)
    personal = PersonalSerializer(read_only=True)
    personal_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Private_training
        fields = "__all__"

    def create(self, validated_data):
        check_personal = validated_data.pop("personal_id")
        personal_found = get_object_or_404(Personal, id=check_personal)

        train_already_exists = Private_training.objects.filter(**validated_data)

        if train_already_exists:
            raise serializers.ValidationError(
                detail="This personal trainer is already scheduled at this hour of this day."
            )

        new_private_training = Private_training.objects.create(
            **validated_data, personal=personal_found
        )

        return new_private_training
