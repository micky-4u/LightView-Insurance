from django.urls import path, include
from django.contrib import admin
from .views import AgentDetails, AgentList, AgentAdd, AgentEdit, AgentRm

urlpatterns = [
    path("", AgentList.as_view()),
    path("<int:pk>", AgentDetails.as_view()),
    path("add/", AgentAdd.as_view()),
    path("edit/<int:pk>", AgentEdit.as_view()),
    path("rm/<int:pk>", AgentRm.as_view()),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]