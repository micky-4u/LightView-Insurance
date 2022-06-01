from django.urls import path
from .views import PolicyTypeDetails,PolicyTypeList, CaseDetails,CaseList,OfferDetails, OfferList



urlpatterns = [
    path("cases", CaseList.as_view()),
    path("cases/<int:pk>", CaseDetails.as_view()),
    path("", PolicyTypeList.as_view()),
    path("/<int:pk>", PolicyTypeDetails.as_view()),
    
]

