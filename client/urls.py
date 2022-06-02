from django.urls import path, include
from django.contrib import admin
from .views import ClientDetails, ClientList, ClientAdd, ClientEdit, ClientRm


urlpatterns = [
    path("", ClientList.as_view()),
    path("<int:pk>", ClientDetails.as_view()),
    path("add", ClientAdd.as_view()),
    path("edit/<int:code>", ClientEdit.as_view()),
    path("rm/<int:code>", ClientRm.as_view()),
]

