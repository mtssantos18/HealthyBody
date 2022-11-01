from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'phone', 'birthdate', 'is_active', 'password', 'email']
        read_only_fields = ('id', 'is_active', 'is_superuser', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}
