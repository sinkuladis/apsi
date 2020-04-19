from datetime import date

from django.forms import ModelForm, DateInput, TextInput, PasswordInput, Select, NullBooleanSelect

from .models import  Users, Countries, Cities

class UsersForm(ModelForm):
    class Meta:
        model   = Users
        fields  = '__all__'
        widgets = {
            'login':        TextInput(attrs={"type": "text"}),
            'password':     PasswordInput(attrs={"type": "text"}),
            'last_name':    TextInput(attrs={"type": "text"}),
            'first_name':   TextInput(attrs={"type": "text"}),
            'city_id':      Select(attrs={"type": "text"}),
            'phone_number': TextInput(attrs={"type": "text"}),
            'email':        TextInput(attrs={"type": "text"}),
            'create_date':  DateInput(attrs={"type": "text"}),
            'active':       NullBooleanSelect(attrs={"type": "text"})
        }

class CountriesForm(ModelForm):
    class Meta:
        model  = Countries
        fields = '__all__'

class CitiesForm(ModelForm):
    class Meta:
        model  = Cities
        fields = '__all__'