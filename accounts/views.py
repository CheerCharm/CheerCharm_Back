from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from CheerCharm.settings import KAKAO_CLIENT_ID, REDIRECT_URI
# Create your views here.


class SignUpView(APIView):
    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data})
        return Response({'message': '회원가입 실패', 'data': serializer.errors})

    def get(self, request):
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response({'message': '유저 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


class LoginView(APIView):
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserLoginSerializer(user)
        return Response({'message': '현재 로그인된 유저 정보 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.validated_data}, status=HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class KaKaoView(APIView):
    def get(self, request):
        kakao_api = "http://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = REDIRECT_URI
        client_id = KAKAO_CLIENT_ID
        return redirect(f'{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}')


class KaKaoCallbackView(APIView):
    def get(self, request):
        data = {
            "grant_type": "authorization_code",
            "client_id": KAKAO_CLIENT_ID,
            "redirect_uri": request.GET["redirect_uri"],
            "code": request.GET["code"]
        }

        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        access_token = requests.post(kakao_token_api, data=data).json()[
            "access_token"]
        print(access_token)
        kakao_user_api = "https://kapi.kakao.com/v2/user/me"
        header = {"Authorization": f"Bearer ${access_token}"}
        user_information = requests.get(kakao_user_api, headers=header).json()
        username = f'cheercharm{user_information["id"]}'
        nickname = user_information["properties"]["nickname"]

        try:
            user = User.objects.get(username=username)
        except:
            user = User(username=username, nickname=nickname,
                        password="temp", id=uuid.uuid4().hex)
            user.save()
            user = User.objects.get(username=username)

        token = RefreshToken.for_user(user)
        data = {
            "id": user.id,
            "username": username,
            "nickname": nickname,
            "access_token": str(token.access_token),
            "refresh_token": str(token)
        }

        return Response({'message': "카카오 로그인 성공", 'data': data}, status=HTTP_200_OK)
