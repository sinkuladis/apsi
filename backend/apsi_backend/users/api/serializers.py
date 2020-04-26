from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

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
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    first_name = serializers.CharField(
            max_length=100,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        email=validated_data['email'],
                                        last_name=validated_data['last_name'],
                                        first_name=validated_data['first_name'],
                                        password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name', 'email', 'password')