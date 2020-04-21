from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)

class Provinces(models.Model):
    name = models.CharField(max_length=100)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

class Cities(models.Model):
    name        = models.CharField(max_length=100)
    country_id  = models.ForeignKey(Countries, on_delete=models.CASCADE)
    province_id = models.ForeignKey(Provinces, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

class UsersCities(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)
