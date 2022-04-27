from django.urls import path 
from django.contrib import admin
from .views import ClientDetails, ClientList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", ClientList.as_view()),
    path("<int:pk>", ClientDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)