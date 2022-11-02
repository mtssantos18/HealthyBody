from django.urls import path
from plans.views import PlanView, PlanDetailView

urlpatterns = [
    path('plan/', PlanView.as_view()),
    path('plan/<pk>/', PlanDetailView.as_view())
]