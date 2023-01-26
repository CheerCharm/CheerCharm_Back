from rest_framework import serializers
from .models import *
from charms.serializers import *


class CheerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Cheer
        fields = ['id', 'charm', 'nickname', 'content', 'created_at']
