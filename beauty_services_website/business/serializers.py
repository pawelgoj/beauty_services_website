from rest_framework import serializers
from .models import Service

# Serialize data to dict and lists
class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    name = serializers.CharField(max_length=100)
    short_description = serializers.CharField(max_length=200)
    long_description = serializers.CharField()
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Service.objects.create(**validated_data)