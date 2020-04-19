from django.db import models
import datetime

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

class Users(models.Model):
    login        = models.CharField(max_length=100)
    password     = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    first_name   = models.CharField(max_length=100)
    city_id      = models.ForeignKey(Cities, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    email        = models.CharField(max_length=100)
    create_date  = models.DateField(default=datetime.date.today)
    active       = models.BooleanField(null=True)

    def __str__(self):
        return 'login: %s | email: %s' % (self.login, self.email)