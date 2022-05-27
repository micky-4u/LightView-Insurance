from django.urls import path, include
from django.contrib import admin
from .views import ClientDetails, ClientList


urlpatterns = [
    path("", ClientList.as_view()),
    path("<int:pk>", ClientDetails.as_view()),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]