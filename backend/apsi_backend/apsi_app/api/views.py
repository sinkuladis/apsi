from rest_framework import status, viewsets, permissions
from django.contrib.auth.models import User
from ..models import Adverts, Advert_Messages
from .serializers import UserSerializer, AdvertSerializer, AdvertMessageSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    fields = ['email', 'username', 'last_name', 'first_name', 'password']

class AdvertView(viewsets.ModelViewSet):
    queryset = Adverts.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ('user_id', 'advert_category_id', 'city_id', 'promotion_id', 'advert_status_id')


class AdvertMessage(viewsets.ModelViewSet):
    queryset = Advert_Messages.objects.all()
    serializer_class = AdvertMessageSerializer
    permission_classes = [permissions.AllowAny]
