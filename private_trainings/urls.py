from django.urls import path
from . import views

urlpatterns = [
    path("customer/private_training/",views.PrivateViewCustomer.as_view()),
    path("private_training/",views.GetAllPrivateTrainings.as_view()),
    path("personal/private_training/",views.PrivateViewPersonal.as_view()),
    path("private_training/<uuid:personal_id>",views.PrivateSchedulePersonal.as_view()),
    path("private_training/personal/<uuid:training_id>",views.PrivateTrainingDetailForPersonals.as_view()),
    path("private_training/customer/<uuid:training_id>",views.PrivateTrainingDetailForCustomers.as_view()),
]
