from rest_framework import serializers
from .models import Claim, ApplicationDoc


class MotoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = ApplicationDoc
        fields = "__all__"

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Claim
        fields = "__all__"

