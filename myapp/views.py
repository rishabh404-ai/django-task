from django.shortcuts import render
from myapp.models import *
from myapp.serializers import *
from rest_framework import viewsets,status,response, permissions
from django.db.models import Prefetch

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Task.objects.all()
    

class TileViewSet(viewsets.ModelViewSet):

    serializer_class = TileSerializer    
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Tile.objects.all()
