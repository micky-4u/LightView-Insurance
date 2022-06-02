from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Client
from client.permissions import IsOwnerOrReadOnly
# from knox.auth import TokenAuthentication
from .serializer import ClientSerializer
# Create your views here.


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class ClientAdd(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class ClientDetails(generics.RetrieveAPIView):
    lookup_field = "client_code"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientEdit(generics.UpdateAPIView):
    lookup_field = "client_code"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ClientRm(generics.DestroyAPIView):
    lookup_field = "client_code"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
