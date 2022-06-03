from django.shortcuts import render
from rest_framework import generics, status
from .models import ApplicationDoc, Claim
from .serializers import HealthSerializer, ClaimSerializer
from rest_framework.response import Response
# Create your views here.
class HealthInsuranceList(generics.ListCreateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = HealthSerializer

    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    
class HealthInsuranceDetails(generics.RetrieveUpdateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = HealthSerializer

class ClaimList(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class= ClaimSerializer
    
    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    

class ClaimDetails(generics.RetrieveAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer