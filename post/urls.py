from django.urls import path
from rest_framework import routers
from .views import PostViewSet, EditorPostViewSet, TTSAPIView, TTSAudioListView, PostCreateView, PostDetailView

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('editorposts', EditorPostViewSet)
# urlpatterns = router.urls

urlpatterns = [

    *router.urls,
    path('api/tts/', TTSAPIView.as_view(), name='tts-api'),
    path('api/tts-list/', TTSAudioListView.as_view(), name='tts-list-api'),
    path('api/create/', PostCreateView.as_view(), name='api-create'),
    path('api/<int:pk>/', PostDetailView.as_view(), name='api-detail'),
    
]