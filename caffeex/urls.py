from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from user import urls as urls_user
from cliente.urls import router as router_cliente
from carro.urls import router as router_carro


router = routers.DefaultRouter()
router.registry.extend(router_cliente.registry)
router.registry.extend(router_carro.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(urls_user)),
]
