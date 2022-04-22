from django.urls import path 
from django.contrib import admin
from .views import AgentDetails, AgentList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", AgentList.as_view()),
    path("<int:pk>", AgentDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)