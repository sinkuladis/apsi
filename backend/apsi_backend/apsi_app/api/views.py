from rest_framework import status, viewsets, permissions
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Advert, AdvertMessage, User, ObservedAds, AdvertCategory
from .serializers import UserSerializer, AdvertSerializer, AdvertMessageSerializer, UserResetPasswordSerializer, \
    ObservedAdsSerializer, AdvertCategorySerializer, AdvertSerializerBrief


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

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthenticated], url_path='current')
    def get_current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class AdvertView(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_fields = ('user', 'advert_category', 'city', 'promotion', 'advert_status')

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertSerializerBrief
        if self.action == 'retrieve':
            return AdvertSerializer
        return AdvertSerializer


class AdvertMessageView(viewsets.ModelViewSet):
    queryset = AdvertMessage.objects.all()
    serializer_class = AdvertMessageSerializer
    permission_classes = [permissions.AllowAny]


class ObservedAdsView(viewsets.ModelViewSet):
    queryset = ObservedAds.objects.all()
    serializer_class = ObservedAdsSerializer
    permission_classes = [permissions.AllowAny]


class AdvertCategoryView(viewsets.ModelViewSet):
    queryset = AdvertCategory.objects.all()
    serializer_class = AdvertCategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]



