from rest_framework import serializers
from .models import *
from charms.serializers import *


class CheerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    charm_nick = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cheer
        fields = ['id', 'charm', 'charm_nick',
                  'nickname', 'content', 'created_at']

    def get_charm_nick(self, obj):
        return obj.charm.user.nickname
