from datetime import date

from django.forms import ModelForm

from .models import Countries, Cities
from django.contrib.auth.models import User

class UsersForm(ModelForm):
    class Meta:
        model   = User
        fields  = ('username',
                   'password',
                   'last_name',
                   'first_name',
                   'email')

class CountriesForm(ModelForm):
    class Meta:
        model  = Countries
        fields = '__all__'

class CitiesForm(ModelForm):
    class Meta:
        model  = Cities
        fields = '__all__'