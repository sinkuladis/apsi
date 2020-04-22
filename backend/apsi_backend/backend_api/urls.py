from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views




urlpatterns = [
    url('login', views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    url('logout', views.LogoutView.as_view(), name='logout'),
]