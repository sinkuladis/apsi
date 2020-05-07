from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]