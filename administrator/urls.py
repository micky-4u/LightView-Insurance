from django.urls import path 
from django.contrib import admin
from .views import UserDetail, UserList, UserRm,RegisterAPI


urlpatterns = [
    path("users", UserList.as_view()),
    path("admins/register", RegisterAPI.as_view()),
    path("users/<int:pk>", UserDetail.as_view()),
    path("users/rm/<int:pk>", UserRm.as_view()),
]

