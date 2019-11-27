from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('empty', views.empty, name="empty"),
    path('', views.home, name="home"),
    path('list-report', views.list_report, name="list_report"),
    path('client_form', views.client_form, name="client_form"),
]
