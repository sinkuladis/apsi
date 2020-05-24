from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Advert, AdvertMessage, AdvertCategory, User


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
 #   advert_category_name = serializers.StringRelatedField(read_only=True)
 #   city_name = serializers.StringRelatedField(read_only=True)
 #   promotion_name = serializers.StringRelatedField(read_only=True)
 #   
 #   advert_status_name = serializers.StringRelatedField(read_only=True)
 #   

    advert_category_name = serializers.ReadOnlyField(source='advert_category.name')
    city_name = serializers.ReadOnlyField(source='city.name')
    promotion_name = serializers.ReadOnlyField(source='promotion.name')
    advert_status_name = serializers.ReadOnlyField(source='advert_status.name')

    user_name = UserSerializer(read_only=True)
    
    subscribing_users = UserSerializer(many=True, read_only=True)


    class Meta:
        model = Advert
        fields = ['id', 'title', 'description', 'price', 'for_free', 'create_date', 'advert_category_name, city_name, promotion_name, user_name, advert_status_name', 'subscribing_users']


class AdvertMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertMessage
        fields = '__all__'
