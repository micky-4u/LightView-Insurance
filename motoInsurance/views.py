from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Claim, Application,Quote
from .serializers import ClaimSerializer, MotoSerializer, QuoteSerializer


# Create your views here.
class MotoInsuranceDetials(generics.RetrieveUpdateAPIView):
    lookup_field = "motoinc_reg"
    queryset = Application.objects.all()
    serializer_class = MotoSerializer


class MotoInsuranceList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = MotoSerializer

class ClaimList(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        
class ClaimDetails(generics.RetrieveAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    
class Quote(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = ClaimSerializer
    

    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
