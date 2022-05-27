from django.urls import path, include
from .views import MotoInsuranceDetials, ClaimList, MotoInsuranceList
urlpatterns = [
    path("",MotoInsuranceList.as_view() ),
    path('<int:pk>',MotoInsuranceDetials.as_view() ),
    path('claims/', ClaimList.as_view() )
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]