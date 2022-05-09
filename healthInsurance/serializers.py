from rest_framework import serializers

from .models import ApplicationDoc, Claim


class HealthSerializer(serializers.ModelSerializer):
    model = ApplicationDoc 
    fields = "__all__"
    
    
class ClaimSerializer(serializers.ModelSerializer):
    model = Claim 
    fields = "__all__"
    
    

