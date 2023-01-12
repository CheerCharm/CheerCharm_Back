from django.urls import path
from .views import *

app_name = 'charms'

urlpatterns = [
    path('charms/', CharmListView.as_view()),
    path('charms/<int:pk>', CharmDetailView.as_view()),
]