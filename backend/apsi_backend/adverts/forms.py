from datetime import date

from django.forms import ModelForm

from apsi_backend.adverts.models import Adverts#, Advert_Categories, Advert_Status, Advert_Messages
#from apsi_backend.users.models import Cities, Countries


class AdvertsForm(ModelForm):
    class Meta:
        model   = Adverts
        fields  = ('title',
                   'description',
                   'price',
                   'for_free',
                   'advert_category_id',
                   'city_id',
                   'create_date',
                   'user_id',
                   'promotion_id',
                   'advert_status_id')

# class AdvertCategoryForm(ModelForm):
#     class Meta:
#         model  = Advert_Categories
#         fields = '__all__'
#
# class AdvertPromotionsForm(ModelForm):
#     class Meta:
#         model  = Advert_Categories
#         fields = '__all__'
#
# class AdvertStatusForm(ModelForm):
#     class Meta:
#         model  = Advert_Status
#         fields = '__all__'
#
# class AdvertMessagesForm(ModelForm):
#     class Meta:
#         model  = Advert_Messages
#         fields = '__all__'
#
# class AdvertMessagesForm(ModelForm):
#     class Meta:
#         model  = Advert_Messages
#         fields = '__all__'
#
#
# class CitiesForm(ModelForm):
#     class Meta:
#         model  = Cities
#         fields = '__all__'