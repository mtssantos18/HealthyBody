from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from personals.models import Personal
from personals.serializers import PersonalAllSerializer
from users.permissions import IsSuperuserOrReadOnly
from rest_framework.response import Response
from personals.permissions import IsSuperuserAllOrPersonalNotDelete, CanNotDeletePersonalUserDeleted
# Create your views here.


class CreateListPersonal(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Personal.objects.all()
    serializer_class = PersonalAllSerializer


class RetrievePatchDeletePersonal(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserAllOrPersonalNotDelete]

    queryset = Personal.objects.all()
    serializer_class = PersonalAllSerializer

    lookup_url_kwarg = "personal_id"

    def perform_destroy(self, instance):
        instance.user.is_active = False
        instance.user.save()

    def delete(self, request, *args, **kwargs):
        personal = self.get_object()
        if personal.user.is_active:
            return super().delete(request, *args, **kwargs)
        return Response({"message": "User already deleted"}, status=400)
