from rest_framework import serializers
from .models import ApplicationDoc

class LifeSerializer(serializers.ModelSerializer):
    model = ApplicationDoc 
    fields = "__all__"
    
class ClaimSerializer(serializers.ModelSerializer):
    pass