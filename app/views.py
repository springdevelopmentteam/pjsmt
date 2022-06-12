from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongSerializer
from .models import Song
# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all() # show data
    serializer_class = SongSerializer # how to show that data