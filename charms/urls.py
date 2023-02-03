from django.urls import path, include
from .views import *

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'upload', ImageUploadView, basename="upload")

app_name = 'charms'

urlpatterns = [
    path('', CharmListView.as_view()),
    path('creating/', CharmNotCreatedListView.as_view()),
    path('created/', CharmCreatedListView.as_view()),
    path('<int:pk>/', CharmDetailView.as_view()),
    path('<int:pk>/upload/', ImageUploadView.as_view()),
    #path('<int:pk>/', include(router.urls)),
]
