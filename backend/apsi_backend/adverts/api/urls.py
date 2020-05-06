from django.urls import path
from . import views as custom_views

urlpatterns = [
    path('', custom_views.AdvertView.as_view(), name='advert-view'),
]