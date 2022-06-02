from django.shortcuts import render
from rest_framework import generics
from .models import Claim, Application,Quote
from .serializers import ClaimSerializer, MotoSerializer, QuoteSerializer


# Create your views here.
class MotoInsuranceDetials(generics.RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = MotoSerializer


class MotoInsuranceList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = MotoSerializer

class ClaimList(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
        
class ClaimDetails(generics.RetrieveAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    
class Quote(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = ClaimSerializer