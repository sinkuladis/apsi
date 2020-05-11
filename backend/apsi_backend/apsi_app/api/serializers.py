from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from ..models import Adverts, Advert_Messages

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
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name', 'email', 'password')

class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adverts
        fields = ('title', 'description', 'price', 'for_free', 'advert_category_id',
                   'city_id', 'create_date', 'user_id', 'promotion_id', 'advert_status_id')

class AdvertMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert_Messages
        fields = ('from_user_id', 'advert_id', 'content')