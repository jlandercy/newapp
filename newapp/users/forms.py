from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = '__all__' # ?


class CustomUserChangeForm(UserChangeForm):

    # https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/

    class Meta:
        model = CustomUser
        fields = ('username', 'email') # ?
