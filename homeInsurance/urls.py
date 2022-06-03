from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomeInsuranceList.as_view()),
    path("<int:homeinc_reg>", HomeInsuranceDetials.as_view()),
    path("claims/", ClaimList.as_view()),
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
]
