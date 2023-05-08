from django import forms
from django.contrib.auth.forms import (AuthenticationForm,
                                       PasswordChangeForm)
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        login = User.login.field.name
        password = User.password.field.name

        fields = (login, password)

        labels = {
            login: 'Логин',
            password: 'Пароль',
        }

        widgets = {
            login: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
            password: forms.PasswordInput(
                attrs={'class': 'form-control',
                       'required': True}),
        }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
