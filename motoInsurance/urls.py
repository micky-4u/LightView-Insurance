from django.urls import path, include

from motoInsurance.models import Quote
from .views import MotoInsuranceDetials, ClaimList, MotoInsuranceList, ClaimDetails, Quote
urlpatterns = [
    path("",MotoInsuranceList.as_view() ),
    path('<int:motoinc_reg>',MotoInsuranceDetials.as_view() ),
    path('claims/', ClaimList.as_view() ),
    path('claims/<int:pk>/', ClaimDetails.as_view() ),
    path('quote/', Quote.as_view() )
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]