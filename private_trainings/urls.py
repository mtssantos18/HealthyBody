from django.urls import path
from . import views

urlpatterns = [
    path("customer/private/", views.PrivateViewCustomer.as_view()),
    path("private_training/", views.GetAllPrivateTrainings.as_view()),
    path("personal/private/", views.PrivateViewPersonal.as_view()),
    path("private_training/<uuid:training_id>", views.PrivateTrainingDetail.as_view()),
]
