from unicodedata import name
# from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', views.logout, name='Logout'),
    path('', include('main.urls'), name='Home')
]