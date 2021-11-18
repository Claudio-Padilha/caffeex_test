from django.urls import path

from user.views.login import Login


urlpatterns = [
    path('login/', Login.as_view())
]
