from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # '' means to show "songs": "http://127.0.0.1:8000/songs/"
    path('api-auth/', include('rest_framework.urls')),
]
