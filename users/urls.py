# "define URL"

from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  # login page
  #url('^login/$', login, {'template_name': 'users/login.html'},    name='login'),
  url('^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  url('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
  url('^register/$', views.register, name='register'),
]




