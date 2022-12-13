from rest_framework import serializers
from .models import Market, Product

class MarketSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    link = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Market.objects.create(**validated_data)


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    exist = serializers.BooleanField(default=False)
    specifies = serializers.CharField(max_length=5000)
    reviews = serializers.CharField(max_length=5000)
    additional_information = serializers.CharField(max_length=5000)
    link = serializers.CharField(max_length=255)
    image_link = serializers.CharField(max_length=255)
    seller = serializers.CharField(max_length=100)