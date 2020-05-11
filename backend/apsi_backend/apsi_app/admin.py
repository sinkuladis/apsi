from django.contrib import admin
from .models import Cities, Countries, Provinces, UsersCities, Adverts, Advert_Categories, Advert_Status, Advert_Messages, Advert_Promotions

# Register your models here.
admin.site.register(Cities)
admin.site.register(Countries)
admin.site.register(Provinces)
admin.site.register(UsersCities)
admin.site.register(Adverts)
admin.site.register(Advert_Categories)
admin.site.register(Advert_Status)
admin.site.register(Advert_Messages)
admin.site.register(Advert_Promotions)