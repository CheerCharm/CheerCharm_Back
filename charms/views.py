from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import *

# Create your views here.


class CharmListView(views.APIView):
    def get(self, request, format=None):
        charms = Charm.objects.filter(user=request.user)
        serializer = CharmSerializer(charms, many=True)
        return Response({'message': '전체 부적 목록 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CharmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '부적 생성 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '부적 생성 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class CharmNotCreatedListView(views.APIView):
    def get(self, request):
        charms = Charm.objects.filter(is_created=False, user=request.user)
        serializer = CharmSerializer(charms, many=True)
        return Response({'message': '생성 중인 부적 목록 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)


class CharmCreatedListView(views.APIView):
    def get(self, request):
        charms = Charm.objects.filter(is_created=True, user=request.user)
        serializer = CharmSerializer(charms, many=True)
        return Response({'message': '생성 완료된 부적 목록 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)


class CharmDetailView(views.APIView):
    def get(self, request, pk, format=None):
        charm = get_object_or_404(Charm, pk=pk)
        serializer = CharmSerializer(charm)
        return Response({'message': '부적 상세 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def delete(self, request, pk):
        charm = get_object_or_404(Charm, pk=pk)
        charm.delete()
        return Response({'message': '부적 삭제 성공'}, status=HTTP_200_OK)
