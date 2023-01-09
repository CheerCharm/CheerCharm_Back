from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.hashers import make_password, check_password

from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','nickname','created_at','updated_at','deleted_at','url_value']

    def create(self, validate_data):
        hashed_password=make_password('password')
        user=User.objects.create(
            nickname=validate_data['nickname'],
            username=validate_data['username'],
            url_value=validate_data['url_value'],
            password=make_password(validate_data['password']),
        )
        # user.make_password(validate_data['password'])
        token = RefreshToken.for_user(user)
        user.refreshtoken = token
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=64)
    password=serializers.CharField(max_length=64, write_only=True)

    def validate(self, data):
        username=data.get("username", None)
        password=data.get("password", None)


        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)
            hashed_password=make_password('password')
            if not check_password(password, user.password):
                raise serializers.ValidationError("not id or password")
        else:
            raise serializers.ValidationError("User does not exist")

        token = RefreshToken.for_user(user=user)
            
        data = {
            'id': user.id,
            'nickname' : user.nickname,
            'url_value':user.url_value,
            'refresh_token' : str(token),
            'access_token' : str(token.access_token)
        }
        return data