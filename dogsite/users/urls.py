from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)

from . import views, forms

app_name = 'users'
urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/log/login.html',
                           authentication_form=forms.UserLoginForm),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='users/log/logout.html'),
         name='logout'),

    path('change_password/',
         PasswordChangeView.as_view(
             template_name='users/password/change_password.html',
             form_class=forms.UserPasswordChangeForm),
         name='change_password'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password/change_password_complete.html'),
         name='change_password_complete'),
]
