from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.contrib.auth import get_user_model

import uuid

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        u = uuid.uuid4()
        user = User.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            id=u.hex
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)
                data = {
                    'username': user.username,
                    'nickname': user.nickname,
                    'id': user.id,
                    'access_token': access,
                    'refresh_token': refresh
                }
                return data
            raise serializers.ValidationError('잘못된 비밀번호')
        else:
            raise serializers.ValidationError('존재하지 않는 유저')
