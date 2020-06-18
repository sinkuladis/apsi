from base64 import b64encode
from io import BytesIO
from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Advert, AdvertMessage, AdvertCategory, User, AdvertPromotion, \
    AdvertStatus, City
from PIL import Image


class CustomizedBase64ImageField(Base64ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, file):
        if file:
            base64 = super().to_representation(file)
            return f'data:image/{file.name.split(".")[1]};base64, {base64}'


class ThumbnailImageField(Base64ImageField):
    def __init__(self, size= (128,128), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size

    def to_representation(self, file):
        from PIL.PngImagePlugin import PngImageFile
        if file:
            img: PngImageFile = Image.open(file)
            img.thumbnail(self.size, Image.ANTIALIAS)
            buffered = BytesIO()
            img.save(buffered, format='png')
            base64 = b64encode(buffered.getvalue()).decode()
            return f'data:image/png;base64, {base64}'


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


class UserSerializerBrief(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class UserResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='user.password', style={'input_type': 'password'},
                                     max_length=20, min_length=8)
    new_password = serializers.CharField(style={'input_type': 'password'},
                                         max_length=20, min_length=8)

    class Meta:
        model = User
        fields = ("password", 'new_password')


# Advert Serializers
class AdvertSerializer(serializers.ModelSerializer):
    image = CustomizedBase64ImageField(represent_in_base64=True, required=False)
    advert_category = serializers.SlugRelatedField(slug_field='name', queryset=AdvertCategory.objects.all())
    city = serializers.SlugRelatedField(slug_field='name', queryset=City.objects.all())
    promotion = serializers.SlugRelatedField(slug_field='name', queryset=AdvertPromotion.objects.all())
    advert_status = serializers.SlugRelatedField(slug_field='name', queryset=AdvertStatus.objects.all())
    user = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=UserSerializerBrief,
    )
    subscribing_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertSerializerBrief(serializers.ModelSerializer):
    advert_category = serializers.SlugRelatedField(slug_field='name', queryset=AdvertCategory.objects.all())
    city = serializers.SlugRelatedField(slug_field='name', queryset=City.objects.all())
    advert_status = serializers.SlugRelatedField(slug_field='name', queryset=AdvertStatus.objects.all())
    user = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=UserSerializerBrief,
    )
    image = ThumbnailImageField(represent_in_base64=True)

    class Meta:
        model = Advert
        fields = ('id', 'advert_category', 'city', 'advert_status', 'user', 'title', 'price', 'image')


class AdvertMessageSerializer(serializers.ModelSerializer):
    advert = serializers.SlugRelatedField(slug_field='title', queryset=Advert.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = AdvertMessage
        fields = '__all__'


class AdvertCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertCategory
        fields = '__all__'

