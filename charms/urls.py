from django.urls import path
from .views import *

app_name = 'charms'

urlpatterns = [
    path('', CharmListView.as_view()),
    path('<uuid:id>/creating/', CharmNotCreatedListView.as_view()),
    path('<uuid:id>/<int:pk>/', CharmDetailView.as_view()),
]
