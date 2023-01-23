from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response

# Create your views here.


class CharmListView(views.APIView):
    def get(self, request, format=None):
        charms = Charm.objects.all()
        serializer = CharmSerializer(charms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CharmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CharmDetailView(views.APIView):
    def get(self, request, pk, format=None):
        charm = get_object_or_404(Charm, pk=pk)
        serializer = CharmSerializer(charm)
        return Response(serializer.data)
