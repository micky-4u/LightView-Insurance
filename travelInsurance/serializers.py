from rest_framework import serializers
from .models import  ApplicationDoc, Claim


class MotoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = ApplicationDoc
        fields = "__all__"

class ClaimSerializer(serializers.ModelSerializer):
    model = Claim
    fields = "__all__"

