from enum import Enum

from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
# User model

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Countries"


class Province(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)


class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Cities"


class User(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)


# Avert model
class AdvertCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Advert categories"


class AdvertPromotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % (self.name)


class AdvertStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = "Advert status"


class Advert(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=9000)
    price = models.FloatField(validators=[MinValueValidator(0.01), MaxValueValidator(1000000)])
    for_free = models.BooleanField(default=False)
    advert_category = models.ForeignKey(AdvertCategory, on_delete=models.CASCADE, related_name='category_name',
                                        null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_name', null=True, blank=True)
    create_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name', null=True, blank=True)
    promotion = models.ForeignKey(AdvertPromotion, on_delete=models.CASCADE, related_name='promotion_name', null=True,
                                  blank=True)
    advert_status = models.ForeignKey(AdvertStatus, on_delete=models.CASCADE, related_name='advert_status_name',
                                      null=True, blank=True)
    subscribing_users = models.ManyToManyField('User', 'subscribing_users')
    image = models.ImageField(blank=True)


    def __str__(self):
        return '%s' % (self.title)


class AdvertMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)

    def __str__(self):
        return '%s' % (self.content[0:20])


class AdvertItems(models.Model):
    advert_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    # quantity = models.PositiveSmallIntegerField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Advert items"
