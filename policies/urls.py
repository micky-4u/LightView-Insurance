from django.urls import path
from .views import PolicyTypeDetails,PolicyTypeList,ProductList,ProductDetails, CaseDetails,CaseList,MotoInsuranceDetials, MotoInsuranceList, OfferDetails, OfferList



urlpatterns = [
    path("", ProductList.as_view()),
    path("<int:pk>", ProductDetails.as_view()),
    path("cases", CaseList.as_view()),
    path("cases/<int:pk>", CaseDetails.as_view()),
    path("policies", PolicyTypeList.as_view()),
    path("policies/<int:pk>", PolicyTypeDetails.as_view()),
    path("motoinsurance/", MotoInsuranceList.as_view()),
    path("motoinsurance/<int:pk>", MotoInsuranceDetials.as_view()),
    
]

