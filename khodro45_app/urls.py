

from django.urls import path
from rest_framework import routers

from khodro45_app.api import   BrandViewSet


# app_name= 'khodro45_app'

router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)


urlpatterns = [
   
    
]+router.urls 