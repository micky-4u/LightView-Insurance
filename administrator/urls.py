from django.urls import path 
from django.contrib import admin
from .views import UserDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", UserList.as_view()),
    path("<int:pk>", UserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)