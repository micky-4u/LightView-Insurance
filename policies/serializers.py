from rest_framework import serializers
from .models import Offers, PolicyType, Products, Case


class OfferSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Offers
        fields = "__all__"
        
class PolicyTypeSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = PolicyType
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Products
        fields = "__all__"
        
class CaseSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Case
        fields = "__all__"
        

