from rest_framework import serializers
from .models import Market

class MarketSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    link = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Market.objects.create(**validated_data)