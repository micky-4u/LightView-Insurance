from django.urls import path
from .views import HealthInsuranceDetails, HealthInsuranceList
urlpatterns = [
    path('health/', HealthInsuranceList.as_view()),
    path('health/<int:pk>', HealthInsuranceDetails.as_view()),
]