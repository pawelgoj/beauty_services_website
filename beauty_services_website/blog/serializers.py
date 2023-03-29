from rest_framework import serializers
from .models import Post

# Serialize data to dict and lists
class PostSerializer(serializers.ModelSerializer):
    # TODO 
    # ADD field images
    # image = serializers.TagSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PostSerializer.objects.create(**validated_data)