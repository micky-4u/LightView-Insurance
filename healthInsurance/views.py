from django.shortcuts import render
from rest_framework import generics
from .models import ApplicationDoc, Claim
from .serializers import HealthSerializer, ClaimSerializer

# Create your views here.
class HealthInsuranceList(generics.ListCreateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = HealthSerializer
    
class HealthInsuranceDetails(generics.RetrieveUpdateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = HealthSerializer

