from rest_framework import generics
from teachers.serializer import TeachersSerializer
from teachers.models import Teacher
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadyOnly



class TeacherView(generics.ListCreateAPIView):

    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadyOnly]

    queryset = Teacher.objects.all()

    serializer_class = TeachersSerializer


class TeacherDetailView(generics.RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadyOnly]

    queryset = Teacher.objects.all()

    serializer_class = TeachersSerializer
    







