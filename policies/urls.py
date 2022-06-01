from django.urls import path
from .views import OfferAdd, OfferRm, PolicyTypeAdd, PolicyTypeDetails,PolicyTypeList, CaseDetails,CaseList,OfferDetails, OfferList



urlpatterns = [
    path("policy", PolicyTypeList.as_view()),
    path("policy/add/", PolicyTypeAdd.as_view()),
    path("policy/<int:pk>", PolicyTypeDetails.as_view()),
    path("policy/cases/", CaseList.as_view()),
    path("policy/cases/<int:policy_type_id>", CaseDetails.as_view()),
    path("offers", OfferList.as_view()),
    path("offers/<int:pk>", OfferDetails.as_view()),
    path("offers/add/", OfferAdd.as_view()),
    path("offers/rm/", OfferRm.as_view()),
    
]

