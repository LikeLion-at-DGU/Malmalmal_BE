from rest_framework import serializers
from .models import IntroWriting

class IntroWritingPreviewSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=50, required=True)
    content = serializers.CharField(required=True)