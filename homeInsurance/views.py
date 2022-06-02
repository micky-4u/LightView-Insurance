from rest_framework import generics
from .models import Claim, ApplicationDocs
from .serializers import ClaimSerializer, HomeSerializer


# Create your views here.
class HomeInsuranceDetials(generics.RetrieveUpdateAPIView):
    lookup_field = "homeinc_code"
    queryset = ApplicationDocs.objects.all()
    serializer_class = HomeSerializer


class HomeInsuranceList(generics.ListCreateAPIView):
    queryset = ApplicationDocs.objects.all()
    serializer_class = HomeSerializer


class ClaimList(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class FileClaim(generics.CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimDetails(generics.RetrieveAPIView):
    lookup_field = "homeinc_code"
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
