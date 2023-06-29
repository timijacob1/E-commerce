from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from classproject.adminapp.models import Product_table
# from.models import Product_table, Profile

class SignUpform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required='false', help_text='optional')
    last_name = forms.CharField(max_length=30, required='false', help_text='optional')
    email = forms.EmailField(max_length=254, help_text= 'Enter a valid email address')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]