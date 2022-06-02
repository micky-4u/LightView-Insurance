from django.urls import path
from .views import OfferAdd, OfferRm, PolicyTypeAdd, PolicyTypeDetails,PolicyTypeList, CaseDetails,CaseList,OfferDetails, OfferList



urlpatterns = [
    path("policy/", PolicyTypeList.as_view()),
    path("policy/add/", PolicyTypeAdd.as_view()),
    path("policy/<int:pk>/", PolicyTypeDetails.as_view()),
    path("policy/cases/", CaseList.as_view()),
    path("policy/cases/<int:pk>/", CaseDetails.as_view()),
    path("offers/", OfferList.as_view()),
    path("offers/<int:offer_code>/", OfferDetails.as_view()),
    path("offers/add/", OfferAdd.as_view()),
    path("offers/rm/<int:offer_code>/", OfferRm.as_view()),
    
]

