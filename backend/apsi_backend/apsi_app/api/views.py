from rest_framework import status, viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Adverts, Advert_Messages
from .serializers import UserSerializer, AdvertSerializer, AdvertMessageSerializer, UserResetPasswordSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    fields = ['id', 'email', 'username', 'last_name', 'first_name']

    @action(detail=True, permission_classes=[IsAuthenticated],
                methods=['put'], url_path='password')
    def reset_user_password(self, request, pk=None):
        reset_password_serializer = UserResetPasswordSerializer(request.user, data=request.data)
        if reset_password_serializer.is_valid(raise_exception=True):
            if not request.user.check_password(request.data.get('password')):
                return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            request.user.set_password(request.data.get('new_password'))
            request.user.save()
            return Response({"Message": ["Password reset successfully"]}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, permission_classes=[IsAuthenticated], url_path='current')
    def get_current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class AdvertView(viewsets.ModelViewSet):
    queryset = Adverts.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ('user_id', 'advert_category_id', 'city_id', 'promotion_id', 'advert_status_id')


class AdvertMessage(viewsets.ModelViewSet):
    queryset = Advert_Messages.objects.all()
    serializer_class = AdvertMessageSerializer
    permission_classes = [permissions.AllowAny]
