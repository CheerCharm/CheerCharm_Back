from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response

from .serializers import *
from charms.serializers import *


class CheerView(APIView):
    def get(self, request, pk):
        cheers = Cheer.objects.filter(charm__id=pk)
        serializer = CheerSerializer(cheers, many=True)
        return Response({'message': '특정 부적에 생성된 응원 목록 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, pk):
        charm = get_object_or_404(Charm, pk=pk)
        charm.cur_cheer = charm.cur_cheer + 1
        if(charm.cur_cheer == charm.total_cheer):
            charm.is_created = True
        charm.save()
        data = {
            'charm': pk,
            'nickname': request.data.get('nickname'),
            'content': request.data.get('content'),
            'cur_cheer': charm.cur_cheer,
            'is_created': charm.is_created
        }
        serializer = CheerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '응원하기 성공', 'data': data}, status=HTTP_200_OK)
        return Response({'message': '응원하기 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class CheerDetailView(APIView):
    def get(self, request, pk):
        cheer = get_object_or_404(Cheer, pk=pk)
        serializer = CheerSerializer(cheer)
        return Response({'message': '응원 개별 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)
