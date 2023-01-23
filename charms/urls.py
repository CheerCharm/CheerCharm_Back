from django.urls import path
from .views import *

app_name = 'charms'

urlpatterns = [
    path('', CharmListView.as_view()),
    path('is_creating/', CharmNotCreatedListView.as_view()),
    path('<int:pk>/', CharmDetailView.as_view()),
]
