from django.urls import path
from .views import *

app_name = 'cheers'

urlpatterns = [
    path('', CheerView.as_view()),
]
