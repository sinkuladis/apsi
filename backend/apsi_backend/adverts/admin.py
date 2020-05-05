from django.contrib import admin
from .models import Adverts, Advert_Status, Advert_Promotions

# Register your models here.
admin.site.register(Adverts)
admin.site.register(Advert_Promotions)
admin.site.register(Advert_Status)
