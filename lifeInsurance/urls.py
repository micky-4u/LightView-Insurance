from django.urls import path, include
from .views import LifeInsuranceDetails, LifeInsuranceList

urlpatterns = [
    path('', LifeInsuranceList.as_view()),
    path('<int:lifeinc_reg>', LifeInsuranceDetails.as_view()),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]