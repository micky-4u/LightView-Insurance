from multiprocessing import Pool
from django.shortcuts import render
from rest_framework import generics, permissions

from .models import PolicyType,Case, Offers
from .serializers import PolicyTypeSerializer, CaseSerializer,OfferSerializer
# Create your views here.


class PolicyTypeList(generics.ListCreateAPIView):
    queryset = PolicyType.objects.all()
    serializer_class = PolicyTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PolicyTypeDetails(generics.RetrieveUpdateAPIView):
    queryset = PolicyType.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PolicyTypeSerializer
    
class CaseList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseDetails(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    
    
class OfferList(generics.ListCreateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class OfferDetails(generics.RetrieveUpdateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    








