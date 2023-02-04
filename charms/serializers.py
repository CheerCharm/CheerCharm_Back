from rest_framework import serializers
from .models import *
from cheers.serializers import *


class ImageSerializer(serializers.ModelSerializer):
    img_front = serializers.URLField(required=False)
    img_back = serializers.URLField(required=False)

    class Meta:
        model = CharmImage
        fields = ['charm', 'img_front', 'img_back']


class CharmSerializer(serializers.ModelSerializer):
    cheer = CheerSerializer(many=True, read_only=True)
    charm_image = ImageSerializer(many=True, read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    nickname = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Charm
        fields = ['id', 'title', 'user', 'username', 'nickname', 'content', 'image', 'total_cheer',
                  'cur_cheer', 'is_created', 'created_at', 'deleted_at', 'cheer', 'charm_image']

    def get_username(self, obj):
        return obj.user.username

    def get_nickname(self, obj):
        return obj.user.nickname
