from django.db import models
from rest_framework import serializers
# Create your models here.
from django.contrib.auth.models import User

from agent.models import Agent

class UserSerializer(serializers.ModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(many =True, queryset = Agent.objects.all())

    class Meta:
        model = User
        fields = "__all__"