from django.contrib import admin
from .models import City, Country, Province, Advert, AdvertCategory, AdvertStatus, AdvertMessage, AdvertPromotion, ObservedAds, AdvertItems

# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(Advert)
admin.site.register(AdvertCategory)
admin.site.register(AdvertStatus)
admin.site.register(AdvertMessage)
admin.site.register(AdvertPromotion)
admin.site.register(ObservedAds)
admin.site.register(AdvertItems)