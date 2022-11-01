from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from modalities.models import Modality
from modalities.permissions import IsAdmPermissionOrTeacherReadOnly
from modalities.serializers import ModalitySerializer


class ModalityView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmPermissionOrTeacherReadOnly]

    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer


class ModalityDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer
