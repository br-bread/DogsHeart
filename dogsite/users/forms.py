from django import forms

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

