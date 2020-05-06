from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from adverts.models import Adverts
from .serializers import AdvertSerializer

class AdvertCreate(APIView):
    """
    Creates the advert.
    """

    def post(self, request, format='json'):
        serializer = AdvertSerializer(data=request.data)
        if serializer.is_valid():
            advert = serializer.save()
            if advert:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # or create class AdvertList?
    def get(self, request, format='json'):
        advert = Adverts.objects.all()
        serializer = AdvertSerializer(advert, many=True)
        return Response(serializer.data)