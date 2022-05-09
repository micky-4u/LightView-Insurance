from django.shortcuts import render
from rest_framework import generics
from .models import ApplicationDoc, Claim
from .serializers import LifeSerializer, ClaimSerializer

# Create your views here.
class LifeInsuranceList(generics.ListCreateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = LifeSerializer
    
class LifeInsuranceDetails(generics.RetrieveUpdateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = LifeSerializer

