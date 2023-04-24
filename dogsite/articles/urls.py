from django.urls import path, re_path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    re_path('(?P<pk>[1-9]\\d*)/$', views.article, name='article'),
    path('breeds/', views.article_list, name='breed_list'),
    re_path('breeds/(?P<pk>[1-9]\\d*)/$', views.article, name='breed'),
]