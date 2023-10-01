from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserCustom

class UserCustomCreationForm(UserCreationForm):

    class Meta:
        model = UserCustom
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address', 'city']