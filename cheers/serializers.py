from rest_framework import serializers
from .models import *

class CheerSerializer(serializers.ModelSerializer): # 임의 설정
    class Meta: # 임의 설정
        model = Cheer # 임의 설정
        fields = ['id', 'charm', 'nickname', 'content'] # 임의 설정