from django.shortcuts import render
from rest_framework import generics
from .models import Agent
from .serializer import AgentSerializer
from rest_framework import permissions
from client.permissions import IsOwnerOrReadOnly


# Create your views here.


class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AgentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]