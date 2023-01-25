from django.urls import path
from .views import *

app_name = 'charms'

urlpatterns = [
    path('', CharmListView.as_view()),
    path('<uuid:url_value>/is_creating/', CharmNotCreatedListView.as_view()),
    path('<uuid:url_value>/<int:pk>/', CharmDetailView.as_view()),
]
