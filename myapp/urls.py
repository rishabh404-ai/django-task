from rest_framework import routers
from django.urls import path
from myapp.views import *

router = routers.DefaultRouter()
router.register('task', TaskViewSet,basename='task')
router.register('tile', TileViewSet,basename='tile')

urlpatterns = [

] + router.urls
