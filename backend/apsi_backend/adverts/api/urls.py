from django.urls import path, include
from rest_framework import routers

from . import views as custom_views

router = routers.DefaultRouter()
router.register('', custom_views.AdvertView)

urlpatterns = [
    path('', include(router.urls)),
]