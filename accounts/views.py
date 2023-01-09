from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework.status import *
from rest_framework import views
from rest_framework.response import Response
 

#jwt를 위해 추가함, install PyJWT
import jwt, datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.

class SignUpView(views.APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})

class LoginView(views.APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=HTTP_200_OK)

class ListView(views.APIView):
    def get(self, request, format=None):
        userlist=User.objects.all()
        serializer=UserSerializer(userlist, many=True)
        return Response(serializer.data)



class LogoutView(views.APIView):

    def post(self, request):
        response = Response({
            "message": "Logout success"
            }, status=HTTP_202_ACCEPTED)
        response.delete_cookie('refreshtoken')

        return response




    

