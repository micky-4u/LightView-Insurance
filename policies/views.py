from multiprocessing import Pool
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import PolicyType,Case, Offers
from .serializers import PolicyTypeSerializer, CaseSerializer,OfferSerializer
# Create your views here.


class PolicyTypeList(generics.ListAPIView):
    queryset = PolicyType.objects.all()
    serializer_class = PolicyTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class PolicyTypeAdd(generics.CreateAPIView):
    queryset = PolicyType.objects.all()
    serializer_class = PolicyTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class PolicyTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PolicyType.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PolicyTypeSerializer
    
class CaseList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    
    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CaseDetails(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    
    
class OfferList(generics.ListAPIView):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class OfferAdd(generics.CreateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    
class OfferDetails(generics.RetrieveUpdateAPIView):
    lookup_field = "offer_code"
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OfferRm(generics.DestroyAPIView):
    lookup_field = "offer_code"
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    








