from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name="home-page"),
    path('index', views.index, name="theme"),
    path('empty', views.empty, name="empty"),
    path('home', views.home, name="home"),
    path('list_report', views.list_report, name="list_report"),
]
