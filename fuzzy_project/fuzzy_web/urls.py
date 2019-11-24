from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name="home-page"),
    path('index', views.index, name="theme"),
    path('empty', views.empty, name="empty"),
]
