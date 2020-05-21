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


class User(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)


# Avert model
class AdvertCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)


class AdvertPromotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % (self.name)


class AdvertStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)


class Advert(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=9000)
    price = models.FloatField(validators=[MinValueValidator(0.01), MaxValueValidator(1000000)])
    for_free = models.BooleanField(default=False)
    advert_category = models.ForeignKey(AdvertCategory, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    promotion = models.ForeignKey(AdvertPromotion, on_delete=models.CASCADE, null=True, blank=True)
    advert_status = models.ForeignKey(AdvertStatus, on_delete=models.CASCADE, null=True, blank=True)
    subscribing_users = models.ManyToManyField('User', 'subscribing_users')

    def __str__(self):
        return '%s' % (self.title)


class AdvertMessage(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)

    def __str__(self):
        return '%s' % (self.content[0:20])
