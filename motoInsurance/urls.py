from django.urls import path, include
from .views import MotoInsuranceDetials, ClaimList
urlpatterns = [
    path('moto/',MotoInsuranceDetials.as_view() ),
    path('claims/', ClaimList.as_view() )
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]