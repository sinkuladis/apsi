from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from adverts.models import Adverts
from .serializers import AdvertSerializer

class AdvertView(viewsets.ModelViewSet):
    queryset = Adverts.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]