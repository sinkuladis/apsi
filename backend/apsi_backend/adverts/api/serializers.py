from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#from django.contrib.auth.models import User
from adverts.models import Adverts


class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adverts
        fields = ('title', 'description', 'price', 'for_free', 'advert_category_id',
                   'city_id', 'create_date', 'user_id', 'promotion_id', 'advert_status_id')

    # title = serializers.CharField(
    #         max_length=200
    #         )
    # description = serializers.CharField(
    #         max_length=9000
    #         )
    # price = serializers.FloatField(
    #         min_length=0.01,
    #         max_length=1000000
    #         )
    # for_free = serializers.BooleanField(
    #
    # )


    # def create(self, validated_data):
    #      advert = Adverts.objects.create_advert(title=validated_data['title'],
    #                                      description=validated_data['description'],
    #                                      price=validated_data['price'])
    #     return advert
