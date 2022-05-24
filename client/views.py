from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Client
from client.permissions import IsOwnerOrReadOnly
# from knox.auth import TokenAuthentication
from .serializer import ClientSerializer
# Create your views here.


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # authentication_classes = (TokenAuthentication,)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

class ClientDetails(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # authentication_classes = (TokenAuthentication,)
