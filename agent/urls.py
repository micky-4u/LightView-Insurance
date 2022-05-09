from django.urls import path, include
from django.contrib import admin
from .views import AgentDetails, AgentList

urlpatterns = [
    path("", AgentList.as_view()),
    path("<int:pk>", AgentDetails.as_view()),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]