from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from personals.models import Personal
from personals.serializers import PersonalAllSerializer
from users.permissions import IsSuperuserOrReadOnly
# Create your views here.


class CreateListPersonal(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Personal.objects.all()
    serializer_class = PersonalAllSerializer
