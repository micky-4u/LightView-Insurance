from django.urls import path, include
from .views import LifeInsuranceDetails, LifeInsuranceList

urlpatterns = [
    path('life/', LifeInsuranceList.as_view()),
    path('life/<int:pk>', LifeInsuranceDetails.as_view()),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]