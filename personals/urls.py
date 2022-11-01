from django.urls import path

from personals import views

urlpatterns = [
    path("", views.CreateListPersonal.as_view())
]
