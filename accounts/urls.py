from .views import *
from django.urls import path

app_name='accounts'

urlpatterns=[
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('list/', ListView.as_view()),
]