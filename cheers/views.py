from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response

from .serializers import *
from charms.serializers import *


class CheerView(APIView):
    def post(self, request):
        charm = get_object_or_404(Charm, pk=request.data.get('charm'))
        charm.cur_cheer = charm.cur_cheer + 1
        if(charm.cur_cheer == charm.total_cheer):
            charm.is_created = True
        charm.save()
        serializer = CheerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'charm': request.data.get('charm'),
                'nickname': request.data.get('nickname'),
                'content': request.data.get('content'),
                'cur_cheer': charm.cur_cheer,
                'is_created': charm.is_created
            }
            return Response({'message': '응원하기 성공', 'data': data}, status=HTTP_200_OK)
        return Response({'message': '응원하기 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
