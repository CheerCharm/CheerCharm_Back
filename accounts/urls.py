from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    #path('kakao/login/', KaKaoView.as_view()),
    path('kakao/login/', KaKaoCallbackView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
