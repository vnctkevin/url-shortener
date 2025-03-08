from .views import shorten_link, redirect_link, register, dashboard, update_profile
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', dashboard, name='home'),
    path('create-link/', shorten_link, name='create-link'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('<str:shortUrl>', redirect_link, name='redirect'),
    path('profile/', update_profile, name='profile'),

    # Microsite URLs
    path('microsites/create/', views.create_microsite, name='create_microsite'),
    path('microsites/<int:pk>/', views.view_microsite, name='view_microsite'),
    path('microsites/<int:pk>/edit/', views.edit_microsite, name='edit_microsite'),
    path('microsites/<int:pk>/delete/', views.delete_microsite, name='delete_microsite'),
]