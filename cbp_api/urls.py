from django.urls import path, include 
from .views import CatViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CatViewSet, basename='cat')
urlpatterns = router.urls