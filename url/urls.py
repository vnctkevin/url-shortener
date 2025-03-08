from .views import shorten_link, redirect_link, register, dashboard
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', dashboard, name='home'),
    path('create-link/', shorten_link, name='create-link'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('<str:shortUrl>', redirect_link, name='redirect'),
]