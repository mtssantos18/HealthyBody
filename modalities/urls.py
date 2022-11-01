from django.urls import path
from modalities import views

urlpatterns = [
    path("modalities/", views.ModalityView.as_view()),
]
