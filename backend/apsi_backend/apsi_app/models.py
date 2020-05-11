from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
#User model

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

    def __str__(self):
        return '%s -- %s' % (self.user_id, self.city_id)

class Subscription_Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)

class UserSubcriptions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    advert_id = models.ForeignKey('Adverts', on_delete=models.CASCADE)
    subscription_status_id = models.ForeignKey(Subscription_Status, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.id)

#Avert model
class Advert_Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)

class Advert_Promotions(models.Model):
    name        = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % (self.name)

class Advert_Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)

class Adverts(models.Model):
    title              = models.CharField(max_length=200)
    description        = models.CharField(max_length=9000)
    price              = models.FloatField(validators=[MinValueValidator(0.01), MaxValueValidator(1000000)])
    for_free           = models.BooleanField(default=False)
    advert_category_id = models.ForeignKey(Advert_Categories, on_delete=models.CASCADE, null=True, blank=True)
    city_id            = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True)
    create_date        = models.DateField(default=datetime.date.today)
    user_id            = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    promotion_id       = models.ForeignKey(Advert_Promotions, on_delete=models.CASCADE, null=True, blank=True)
    advert_status_id   = models.ForeignKey(Advert_Status, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.title)

class Advert_Messages(models.Model):
    from_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    advert_id    = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    content      = models.CharField(max_length=3000)

    def __str__(self):
        return '%s' % (self.content[0:20])