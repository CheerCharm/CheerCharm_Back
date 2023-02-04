from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.viewsets import ViewSet

import boto3
from CheerCharm.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_STORAGE_REGION

# Create your views here.


class CharmListView(views.APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        charms = Charm.objects.filter(is_created=False, user=request.user)
        serializer = CharmSerializer(charms, many=True)
        return Response({'message': '생성 중인 부적 목록 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)


class CharmCreatedListView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        charms = Charm.objects.filter(is_created=True, user=request.user)
        serializer = CharmSerializer(charms, many=True)
        return Response({'message': '생성 완료된 부적 목록 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)


class CharmDetailView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        charm = get_object_or_404(Charm, pk=pk)
        serializer = CharmSerializer(charm)
        return Response({'message': '부적 상세 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def delete(self, request, pk):
        charm = get_object_or_404(Charm, pk=pk)
        charm.delete()
        return Response({'message': '부적 삭제 성공'}, status=HTTP_200_OK)


class S3ImgUploader:
    def __init__(self, file, url):
        self.file = file
        self.url = url

    def upload(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

        s3_client.upload_fileobj(
            self.file,
            AWS_STORAGE_BUCKET_NAME,
            self.url,
            ExtraArgs={
                "ContentType": self.file.content_type
            }
        )
        print(s3_client)
        return f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_STORAGE_REGION}.amazonaws.com/{self.url}'


class ImageUploadView(views.APIView):
    def get(self, request, pk):
        charm_image = get_object_or_404(CharmImage, charm__id=pk)
        serializer = ImageSerializer(charm_image)
        return Response({'message': '부적 이미지 링크 보기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, pk):
        charm = get_object_or_404(Charm, pk=pk)
        file_front = request.FILES.get('file_front')
        file_back = request.FILES.get('file_back')

        url = str(charm.user.id) + "-" + str(charm.id)
        img_front = S3ImgUploader(file_front, url+"-f").upload()
        img_back = S3ImgUploader(file_back, url+"-b").upload()

        data = {
            'charm': pk,
            'img_front': img_front,
            'img_back': img_back
        }
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '이미지 업로드 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '이미지 업로드 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
