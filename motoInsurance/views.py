from django.shortcuts import render
from rest_framework import generics
from .models import MotoInsurance
from .serializers import MotoSerializer


# Create your views here.
class MotoInsuranceDetials(generics.RetrieveUpdateAPIView):
    queryset = MotoInsurance.objects.all()
    serializer_class = MotoSerializer


class MotoInsuranceList(generics.ListCreateAPIView):
    queryset = MotoInsurance.objects.all()
    serializer_class = MotoSerializer
