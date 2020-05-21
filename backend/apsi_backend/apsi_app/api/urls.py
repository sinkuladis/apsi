from django.urls import path, include
from rest_framework import routers
from . import views as custom_views

router = routers.DefaultRouter()
router.register('users', custom_views.UserView)
router.register('adverts', custom_views.AdvertView)
router.register('adverts/messages', custom_views.AdvertMessageView)

urlpatterns = [
    path('', include(router.urls)),
]