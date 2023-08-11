from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework.validators import UniqueValidator

from django.contrib.auth import authenticate
from .models import Profile, EditorProfile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', "password", "password2")
        
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"비밀번호가 일치하지 않습니다!"}
            )
        
        return data
    
    def create(self, validated_data):
        username = validated_data['username']
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "이미 존재하는 사용자입니다."})
        
        user = User.objects.create_user(username=username)
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "로그인 실패! 아이디 또는 비밀번호가 틀립니다."}
        )
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( 'birthday', 'nickname', 'address')
        

class EditorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorProfile
        fields = ( 'name', 'address')