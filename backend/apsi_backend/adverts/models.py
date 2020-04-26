from django.db import models
from apsi.backend.apsi_backend.users.models import UsersCities
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

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

class Advert_Messages(models.Model):
    from_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    advert_id    = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    content      = models.CharField(max_length=3000)

class Adverts(models.Model):
    title              = models.CharField(max_length=200)
    description        = models.CharField(max_length=9000)
    price              = models.FloatField(validators=[MinValueValidator(0.01), MaxValueValidator(1000000)])
    for_free           = models.BooleanField(default=False)
    advert_category_id = models.ForeignKey(Advert_Categories, on_delete=models.CASCADE)
    city_id            = models.ForeignKey(UsersCities, on_delete=models.CASCADE)
    create_date        = models.DateField(default=datetime.date.today)
    user_id            = models.ForeignKey(User, on_delete=models.CASCADE)
    promotion_id       = models.ForeignKey(Advert_Promotions, on_delete=models.CASCADE, null=True)
    advert_status_id   = models.ForeignKey(Advert_Status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % (self.marchant_name)