from rest_framework import serializers
from .models import MotoInsurance


class MotoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = MotoInsurance
        fields = "__all__"
