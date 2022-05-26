from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import generics
# from knox.auth import TokenAuthentication
from rest_framework import permissions
# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, ]

class UserDetail(generics.RetrieveAPIView):
    def getUser(self, pk):
        pass
    queryset = User.objects.all()
    serializer_class = UserSerializer