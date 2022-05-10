from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our API View"""
    name=serializers.Charfield(max_length=10)