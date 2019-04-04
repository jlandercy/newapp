from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.validators import RegexValidator

# https://regex101.com/
avatarValidator = RegexValidator(r"^&#[x]{0,1}[\da-fA-f]{2,5};$", "Avatar code is a HTML symbol, see https://www.toptal.com/designers/htmlarrows/symbols/")

class CustomUserCreationForm(UserCreationForm):

    tosaccepted = forms.BooleanField()
    avatatcode = forms.CharField(
        #validators=[]
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'tosaccepted', 'avatarcode')


class CustomUserChangeForm(UserChangeForm):

    avatatcode = forms.CharField(
        #validators=[]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatarcode')
