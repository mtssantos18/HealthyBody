from rest_framework import generics
from .models import Class
from .serializers import ListClassSerializer, PostClassSerializer

from rest_framework.authentication import TokenAuthentication

from utils.mixins import SerializerByMethodMixin

from classes.permissions import CustomPermission


class ClassView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    queryset = Class.objects.all()
    serializer_map = {
        "GET": ListClassSerializer,
        "POST": PostClassSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teacher)


class ClassDetailView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ...
