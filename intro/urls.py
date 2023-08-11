from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import IntroWritingPreviewViewSet

router = DefaultRouter()
router.register('preview', IntroWritingPreviewViewSet, basename='intro-writing-preview')

urlpatterns = router.urls
