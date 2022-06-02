from django.urls import path 
from django.contrib import admin
from .views import UserDetail, UserList, UserRm


urlpatterns = [
    path("", UserList.as_view()),
    path("<int:pk>", UserDetail.as_view()),
    path("rm/<int:pk>", UserRm.as_view()),
]

