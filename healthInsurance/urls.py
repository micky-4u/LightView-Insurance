from django.urls import path

from .views import HealthInsuranceDetails, HealthInsuranceList, ClaimList, ClaimDetails


urlpatterns = [
    path('', HealthInsuranceList.as_view()),
    path('<int:pk>', HealthInsuranceDetails.as_view()),
    path('claims/', ClaimList.as_view()),
    path('claims/<int:pk>', ClaimDetails.as_view()),
]