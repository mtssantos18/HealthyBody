from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import MyCustomPermissionCustomer,SuperUserPermission,MyCustomPermissionPersonal

from .serializer import PrivateSerializer
from .models import Private_training
from utils.mixins import SerializerByMethodMixin

class PrivateViewCustomer(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomer]

    queryset = Private_training.objects
    serializer_class = PrivateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(customer=self.request.user)

class GetAllPrivateTrainings(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermission]

    queryset = Private_training.objects.all()
    serializer_class = PrivateSerializer

class PrivateViewPersonal(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionPersonal]

    queryset = Private_training.objects
    serializer_class = PrivateSerializer

class PrivateTrainingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_url_kwarg = "training_id"

    queryset = Private_training.objects
    serializer_class = PrivateSerializer
