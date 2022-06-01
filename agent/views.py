from django.shortcuts import render
from rest_framework import generics
from .models import Agent
from .serializer import AgentSerializer
from rest_framework import permissions
from client.permissions import IsOwnerOrReadOnly
# from knox.auth import TokenAuthentication

# Create your views here.


class AgentList(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class AgentDetails(generics.RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class AgentAdd(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class AgentRm(generics.DestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class AgentEdit(generics.UpdateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]