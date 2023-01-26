from django.urls import path
from .views import *

app_name = 'cheers'

urlpatterns = [
    path('<int:pk>/', CheerView.as_view()),
    path('detail/<int:pk>/', CheerDetailView.as_view()),
]
