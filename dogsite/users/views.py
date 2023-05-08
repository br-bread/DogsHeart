from django.shortcuts import render, redirect
from . import forms
from .models import User


def sign_up(request):
    template_name = 'users/signup.html'
    form = forms.SignupForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']

        User.objects.create_user(login, password)
        return redirect('homepage:home')

    return render(request, template_name, context)
