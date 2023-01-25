from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('kakao/login/', KaKaoView.as_view()),
    path('kakao/callback/', KaKaoCallbackView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]
