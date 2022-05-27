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

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class ClientDetails(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = (TokenAuthentication,)
