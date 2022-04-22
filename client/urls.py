from django.urls import path 
from django.contrib import admin
from .views import ClientDetails, ClientList


urlpatterns = [
    path("agent/", ClientList.as_view()),
    path("agent/<int:pk>", ClientDetails.as_view()),
]
