from multiprocessing.connection import Client
from rest_framework import serializers
from .models import Client
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = "created_by.username")
    class Meta:
        model = Client
        fields = "__all__"
