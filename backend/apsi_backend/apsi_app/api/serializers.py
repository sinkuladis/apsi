from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Advert, AdvertMessage, AdvertCategory, User, City, AdvertPromotion, AdvertStatus


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=30,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    last_name = serializers.CharField(
        max_length=100,
    )
    first_name = serializers.CharField(
        max_length=100,
    )
    password = serializers.CharField(style={'input_type': 'password'},
                                     max_length=20, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name', 'email', 'password', 'city')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='user.password', style={'input_type': 'password'},
                                     max_length=20, min_length=8)
    new_password = serializers.CharField(style={'input_type': 'password'},
                                         max_length=20, min_length=8)

    class Meta:
        model = User
        fields = ("password", 'new_password')


class AdvertSerializer(serializers.ModelSerializer):

    advert_category = serializers.SlugRelatedField(slug_field='name', queryset=AdvertCategory.objects.all())
    city = serializers.SlugRelatedField(slug_field = 'name', queryset=City.objects.all())
    promotion = serializers.SlugRelatedField(slug_field = 'name', queryset=AdvertPromotion.objects.all())
    advert_status = serializers.SlugRelatedField(slug_field = 'name', queryset=AdvertStatus.objects.all())
    user = serializers.SlugRelatedField(slug_field = 'username', queryset=User.objects.all())

    

    
    subscribing_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertMessage
        fields = '__all__'
