from rest_framework.serializers import ModelSerializer, ValidationError

from personals.models import Personal
from users.models import User
from users.serializers import UserSerializer


class PersonalAllSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Personal
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        validated_data["user"] = user

        personal = Personal.objects.create(**validated_data)
        return personal

    def update(self, instance, validated_data):
        try:
            request_user = validated_data.pop("user")
        except KeyError:
            request_user = False

        if request_user:
            for key, value in request_user.items():
                setattr(instance.user, key, value)
            instance.user.save()

        super().update(instance, validated_data)
        return instance
