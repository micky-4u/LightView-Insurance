from rest_framework import serializers
from .models import Claim, ApplicationDocs


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocs
        fields = "__all__"


class ClaimSerializer(serializers.ModelSerializer):
    model = Claim
    fields = "__all__"

