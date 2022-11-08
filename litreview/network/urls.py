from django.urls import path
from django.contrib import admin

from network import views

app_name = 'network'
urlpatterns = [
    path('subscription/', views.UserNetwork.as_view(), name='subscription'),
    path('unfollow/', views.UnfollowUser.as_view(), name='unfollow'),
]