from rest_framework import serializers
from users.serializers import ProfileSerializer, EditorProfileSerializer
from .models import Post, Editor_Post, User, Profile, EditorProfile


class PostSerializer(serializers.ModelSerializer):
    # nickname = ProfileSerializer(read_only=True)
    # author = ProfileSerializer()
    class Meta:
        model = Post
        fields = ('published_date', 'like', 'title', 'content')
        read_only_fields = ( 'published_date', 'like')
        
        

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')
        

class EditorPostSerializer(serializers.ModelSerializer):
    # name = EditorProfileSerializer(read_only=True)
    # author = EditorProfileSerializer()
    class Meta:
        model = Editor_Post
        fields = ('published_date', 'like', 'scarp', 'title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
        read_only_fields = ('published_date', 'like', 'scarp', 'image')


class EditorPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor_Post
        fields = ('title', 'content', 'date', 'recruit_date', 'place', 'phone_number', 'image')
    
