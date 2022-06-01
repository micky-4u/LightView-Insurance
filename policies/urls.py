from django.urls import path
from .views import PolicyTypeAdd, PolicyTypeDetails,PolicyTypeList, CaseDetails,CaseList,OfferDetails, OfferList



urlpatterns = [
    path("", PolicyTypeList.as_view()),
    path("add/", PolicyTypeAdd.as_view()),
    path("/<int:pk>", PolicyTypeDetails.as_view()),
    path("cases/", CaseList.as_view()),
    path("cases/<int:policy_type_id>", CaseDetails.as_view()),
    
]

