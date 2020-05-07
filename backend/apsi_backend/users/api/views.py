from django.contrib.auth.models import User
from rest_framework import status, viewsets

from users.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    fields = ['email', 'username','last_name', 'first_name', 'password']



