from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/log/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='users/log/logout.html'),
         name='logout'),

    path('change_password/',
         PasswordChangeView.as_view(
             template_name='users/password/change_password.html'),
         name='change_password'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password/change_password_complete.html'),
         name='change_password_complete'),
]
