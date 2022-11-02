from django.shortcuts import render
from rest_framework import generics
from teachers.serializer import TeachersSerializer
from teachers.models import Teacher


class TeacherView(generics.ListCreateAPIView):

    queryset = Teacher.objects.all()

    serializer_class = TeachersSerializer
