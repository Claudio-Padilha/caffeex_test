from django.urls import path, include
from rest_framework import routers

from cliente.views.clenteViewset import ClienteViewSet


router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
