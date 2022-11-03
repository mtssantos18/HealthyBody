from django.urls import path

from trains import views

urlpatterns = [
    path("trains/", views.CreateListTrainView.as_view()),
    # path("personal/<pk>/", views.RetrievePatchDeletePersonal.as_view()),
]
