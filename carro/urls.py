from django.urls import path, include
from rest_framework import routers

from carro.views.carroViewSet import CarroViewSet

router = routers.DefaultRouter()
router.register(r'carro', CarroViewSet)
