from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer, ValidationError

from customers.models import Customer
from users.models import User
from plans.models import Plan
from users.serializers import UserSerializer
from plans.serializers import PlanSerializer
import ipdb

class CustomerSerializer(ModelSerializer):
    user = UserSerializer()
    plan = PlanSerializer(read_only=True)
    plan_id = serializers.UUIDField(write_only = True)

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        check_plan = validated_data.pop("plan_id")
        plan_found = get_object_or_404(Plan, id=check_plan)

        user = User.objects.create_user(**user_data)

        validated_data["user"] = user

        customer = Customer.objects.create(**validated_data, plan = plan_found)
        return customer

class CustomerDetailSerializer(ModelSerializer):
    user = UserSerializer()
    plan = PlanSerializer(read_only=True)
    plan_id = serializers.UUIDField(write_only = True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "user",
            "plan",
            "plan_id"
        ]
        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        try:
            request_user = validated_data.pop("user")
        except KeyError:
            request_user = False

        try:
            check_plan = validated_data.pop("plan_id")
        except KeyError:
            check_plan = False
                   
        if check_plan:
            plan_found = get_object_or_404(Plan, id=check_plan)
            setattr(instance, "plan", plan_found)
            instance.save()

        if request_user:
            for key, value in request_user.items():
                setattr(instance.user, key, value)
            instance.user.save()

        return instance