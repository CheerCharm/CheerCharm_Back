from rest_framework import serializers
from .models import *
from cheers.serializers import *

class CharmSerializer(serializers.ModelSerializer):
    cheer = CheerSerializer(many=True, read_only=True)
    class Meta:
        model = Charm
        fields = ['id', 'title', 'user', 'content', 'image', 'total_cheer', 'cur_cheer', 'is_created', 'created_at', 'deleted_at', 'cheer']