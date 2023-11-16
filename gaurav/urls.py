from django.contrib import admin
from django.urls import path,include
from gaurav.views import companyViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',companyViewSet)

urlpatterns = [
     
       path('',include(router.urls))
   
]
