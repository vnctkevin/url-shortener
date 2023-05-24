from .views import shorten_link, redirect_link
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', shorten_link, name='shorten'),
    path('<str:shortUrl>', redirect_link, name='redirect')
]