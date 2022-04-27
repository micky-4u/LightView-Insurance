from django.urls import path
from .views import PolicyTypeDetails,PolicyTypeList,ProductList,ProductDetails, CaseDetails,CaseList,MotoInsuranceDetials, MotoInsuranceList, OfferDetails, OfferList

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", ProductList.as_view()),
    path("<int:pk>", ProductDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)