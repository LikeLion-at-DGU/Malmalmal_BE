import os

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import Profile, EditorProfile
from .models import Post, Editor_Post, TTSAudio, TTSAudioTitle
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer, EditorPostSerializer, EditorPostCreateSerializer, TTSAudioSerializer, TTSAudioTitleSerializer

from django.conf import settings
from gtts import gTTS


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = []
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=profile)

    
        
        
class EditorPostViewSet(viewsets.ModelViewSet):
    queryset = Editor_Post.objects.all()
    permission_classes = []
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EditorPostSerializer
        return EditorPostCreateSerializer
    
    def perform_create(self, serializer):
        editor_profile = EditorProfile.objects.get(user=self.request.user)  
<<<<<<< HEAD
        serializer.save(editor_profile=editor_profile)
        
=======
        serializer.save(author=self.request.user, editor_profile=editor_profile)


# tts 관련
class TTSAPIView(APIView):
    def post(self, request):
        tts_title_message = request.data.get('tts_title_message')
        tts_message = request.data.get('tts_message')

        if tts_title_message:
            tts_title = gTTS(text=tts_title_message, lang='ko')
            tts_title_audio = TTSAudioTitle(title_message=tts_title_message, user=request.user)
            tts_title_audio.save()

            tts_folder = os.path.join(settings.MEDIA_ROOT, 'tts_title')
            os.makedirs(tts_folder, exist_ok=True)

            save_path = os.path.join(tts_folder, f'tts_title_{tts_title_audio.id}.mp3')
            tts_title.save(save_path)

            tts_title_audio.audio_file = f'tts_title/tts_title_{tts_title_audio.id}.mp3'
            tts_title_audio.save()

        if tts_message:
            tts = gTTS(text=tts_message, lang='ko')
            tts_audio = TTSAudio(message=tts_message, user=request.user)
            tts_audio.save()

            tts_folder = os.path.join(settings.MEDIA_ROOT, 'tts')
            os.makedirs(tts_folder, exist_ok=True)

            save_path = os.path.join(tts_folder, f'tts_{tts_audio.id}.mp3')
            tts.save(save_path)

            tts_audio.audio_file = f'tts/tts_{tts_audio.id}.mp3'
            tts_audio.save()

        return Response(status=status.HTTP_201_CREATED)


class TTSAudioListView(APIView):
    def get(self, request):
        audios = TTSAudio.objects.all()
        serializer = TTSAudioSerializer(audios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated] #로그인 유저만

    def post(self, request):
        post_serializer = PostSerializer(data=request.data, context={'request': request})
        if post_serializer.is_valid():
            post = post_serializer.save(writer=request.user)
            
            tts_title_message = request.data.get('tts_title_message')
            tts_message = request.data.get('tts_message')
            
            if tts_title_message:
                existing_tts_title = TTSAudioTitle.objects.filter(title_message=tts_title_message, user=request.user).first()
                if not existing_tts_title:
                    tts_title = gTTS(text=tts_title_message, lang='ko')
                    tts_title_audio = TTSAudioTitle(title_message=tts_title_message, user=request.user)
                    tts_title_audio.save()

                    tts_folder = os.path.join(settings.MEDIA_ROOT, 'tts_title')
                    os.makedirs(tts_folder, exist_ok=True)

                    save_path = os.path.join(tts_folder, f'tts_title_{tts_title_audio.id}.mp3')
                    tts_title.save(save_path)

                    tts_title_audio.audio_file = f'tts_title/tts_title_{tts_title_audio.id}.mp3'
                    tts_title_audio.save()

                    post.tts_title_audio = tts_title_audio
                    post.save()
            
            if tts_message:
                existing_tts_audio = TTSAudio.objects.filter(message=tts_message, user=request.user).first()
                if not existing_tts_audio:
                    tts = gTTS(text=tts_message, lang='ko')
                    tts_audio = TTSAudio(message=tts_message, user=request.user)
                    tts_audio.save()

                    tts_folder = os.path.join(settings.MEDIA_ROOT, 'tts')
                    os.makedirs(tts_folder, exist_ok=True)

                    save_path = os.path.join(tts_folder, f'tts_{tts_audio.id}.mp3')
                    tts.save(save_path)

                    tts_audio.audio_file = f'tts/tts_{tts_audio.id}.mp3'
                    tts_audio.save()

                    post.tts_audio = tts_audio
                    post.save()

            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]  # 누구나 조회 가능하도록 설정
>>>>>>> 2ee1fcf9e453c0900af0cd023e78d9b53ea05301
