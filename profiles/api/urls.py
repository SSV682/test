from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'news',views.NewsViewSet)

app_name = 'profiles' 

urlpatterns = [
    path('', include(router.urls)),
    
]