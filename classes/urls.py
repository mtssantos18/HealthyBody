from django.urls import path
from classes import views

urlpatterns = [
    path("class/", views.ClassView.as_view()),
    path("class/<class_id>/", views.ClassDetailView.as_view()),
]
