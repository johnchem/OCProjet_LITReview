from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('main/', views.main, name='landing'),
    path('feed/', views.feed, name='feed')
]