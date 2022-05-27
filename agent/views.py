from django.shortcuts import render
from rest_framework import generics
from .models import Agent
from .serializer import AgentSerializer
from rest_framework import permissions
from client.permissions import IsOwnerOrReadOnly
# from knox.auth import TokenAuthentication

# Create your views here.


class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, ]
    

class AgentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]