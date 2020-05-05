from django.urls import path
from . import views as custom_views
from rest_framework.authtoken import views

urlpatterns = [
    path('create', custom_views.UserCreate.as_view(), name='account-create'),
    path('login', views.obtain_auth_token, name='login'),
]