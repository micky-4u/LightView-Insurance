from multiprocessing.connection import Client
from rest_framework import serializers
from .models import Agent
from client.models import Client

class AgentSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source = "created_by.username")
    # clients = serializers.PrimaryKeyRelatedField(many =True, queryset = Client.objects.all())
    
    class Meta:
        model = Agent
        fields = "__all__"
