from rest_framework.serializers import ModelSerializer, ValidationError

from personals.models import Personal


class PersonalAllSerializer(ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'
        depth = 1
        read_only_fields = ['id']
