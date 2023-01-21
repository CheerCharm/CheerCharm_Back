from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response

from .serializers import *


class CheerView(APIView):
    def post(self, request, pk):
        serializer = CheerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '응원하기 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '응원하기 실패', 'data': serializer.data}, status=HTTP_400_BAD_REQUEST)
