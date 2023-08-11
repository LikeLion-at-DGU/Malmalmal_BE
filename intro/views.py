from django.shortcuts import render
from .serializers import IntroWritingPreviewSerializer
# Create your views here.


from rest_framework import viewsets
from rest_framework.response import Response

class IntroWritingPreviewViewSet(viewsets.ViewSet):
    serializer_class = IntroWritingPreviewSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        preview_data = serializer.validated_data
        return Response(preview_data)
