from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework.validators import UniqueValidator

from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    birthday = serializers.DateField(required=True)
    address = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', "password", "password2", "birthday", "address", "nickname")
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"비밀번호가 일치하지 않습니다!"}
            )
        
        return data
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token, created = Token.objects.get_or_create(user=user)
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
            {"error": "로그인 실패ㅠㅠ 아이디 또는 비밀번호가 틀립니다."}
        )
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'birthday', 'nickname', 'address')
        

class EditorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'address')