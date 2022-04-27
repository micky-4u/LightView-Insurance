from django.urls import path 
from django.contrib import admin
from .views import ClientDetails, ClientList


urlpatterns = [
    path("", ClientList.as_view()),
    path("<int:pk>", ClientDetails.as_view()),
]

