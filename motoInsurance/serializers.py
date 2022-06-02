from rest_framework import serializers
from .models import Claim, Application, Quote, Claim


class MotoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Application
        fields = "__all__"

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Claim
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Quote
        fields = "__all__"

        

