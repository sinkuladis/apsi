from django.contrib import admin
from .models import City, Country, Province, Advert, AdvertCategory, AdvertStatus, AdvertPromotion, AdvertItems

# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(Advert)
admin.site.register(AdvertCategory)
admin.site.register(AdvertItems)