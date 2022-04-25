

from atexit import register
from django.urls import path
from rest_framework import routers

from khodro45_app.api import   AuctionView, BrandViewSet



# app_name= 'khodro45_app'

router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'auction',AuctionView)


urlpatterns = [
   
    
]+router.urls 