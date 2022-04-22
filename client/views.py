from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializer import ClientSerializer
# Create your views here.


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

class ClientDetails(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer