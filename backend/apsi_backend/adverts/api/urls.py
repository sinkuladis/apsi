from django.urls import path
from . import views as custom_views

urlpatterns = [
    path('create', custom_views.AdvertCreate.as_view(), name='advert-create'),
]