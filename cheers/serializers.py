from rest_framework import serializers
from .models import *


class CheerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheer
        fields = ['charm', 'nickname', 'content']
