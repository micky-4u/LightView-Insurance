from django.shortcuts import render
from rest_framework import generics
from .models import Claim, ApplicationDoc
from .serializers import ClaimSerializer, MotoSerializer


# Create your views here.
class MotoInsuranceDetials(generics.RetrieveUpdateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = MotoSerializer


class MotoInsuranceList(generics.ListCreateAPIView):
    queryset = ApplicationDoc.objects.all()
    serializer_class = MotoSerializer

class ClaimList(generics.ListAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    
class FileClaim(generics.CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    
class ClaimDetails(generics.RetrieveAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer