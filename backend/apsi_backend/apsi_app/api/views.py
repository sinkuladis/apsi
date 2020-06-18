from rest_framework import status, viewsets, permissions
from rest_framework.decorators import  action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Advert, AdvertMessage, User, AdvertCategory
from .serializers import UserSerializer, AdvertSerializer, AdvertMessageSerializer, UserResetPasswordSerializer, \
    AdvertCategorySerializer, AdvertSerializerBrief
from ..permissions import IsSelf, IsOwner, IsMessageOwner, IsMessageReceiver


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    fields = ['id', 'email', 'username', 'last_name', 'first_name']

    def get_permissions(self):
        if self.action in ['update','partial_update','destroy']:
            self.permission_classes = [IsSelf, permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny,]
        return super(self.__class__, self).get_permissions()

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('title', 'user', 'user_name', 'advert_category', 'city', 'promotion', 'advert_status', 'subscribing_users')


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer_class()(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertSerializerBrief
        if self.action == 'retrieve':
            return AdvertSerializer
        return AdvertSerializer

    def get_permissions(self):
        if self.action in ['update','partial_update','destroy']:
            self.permission_classes = [IsOwner, permissions.IsAdminUser]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
        return super(self.__class__, self).get_permissions()

    @action(detail=True, permission_classes=[IsAuthenticated],
            methods=['post', 'delete'], url_path='observed')
    def add_to_favourite(self, request, pk=None):
        if request.method == 'POST':
            instance: Advert = self.get_object()
            instance.subscribing_users.add(request.user)
            return Response(status=status.HTTP_200_OK)
        if request.method == 'DELETE':
            instance: Advert = self.get_object()
            instance.subscribing_users.remove(request.user)
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AdvertMessageView(viewsets.ModelViewSet):
    queryset = AdvertMessage.objects.all()
    serializer_class = AdvertMessageSerializer

    def get_permissions(self):
        if self.action in ['update','partial_update','destroy']:
            self.permission_classes = [IsMessageOwner]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [IsMessageOwner, IsMessageReceiver]
        return super(self.__class__, self).get_permissions()


class AdvertCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = AdvertCategory.objects.all()
    serializer_class = AdvertCategorySerializer
    permission_classes = [permissions.AllowAny]


class AdvertLatest(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by('-create_date')[:10]
    serializer_class = AdvertSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ('user', 'advert_category', 'city', 'promotion', 'advert_status')

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertSerializerBrief
        if self.action == 'retrieve':
            return AdvertSerializer
        return AdvertSerializer

