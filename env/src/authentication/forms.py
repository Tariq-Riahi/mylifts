from django import forms
from django.forms import CheckboxInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from lifters.models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(datetime.now().year-100, datetime.now().year+1)), initial=datetime.now().today(), required=True)
    metric = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "metric")
        widgets = {
            'metric': CheckboxInput(attrs={
                'class': "form-check-input",
            })
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }