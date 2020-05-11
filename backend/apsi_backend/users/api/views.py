from django.contrib.auth.models import User
from rest_framework import status, viewsets, permissions

from users.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    fields = ['email', 'username','last_name', 'first_name', 'password']



