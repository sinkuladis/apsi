from django.contrib import admin
from .models import Users, Cities, Countries

# Register your models here.
admin.site.register(Users)
admin.site.register(Cities)
admin.site.register(Countries)