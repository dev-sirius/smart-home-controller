
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^temp', views.index, name="index"),
    url(r'^api/sensors', views.API, name="API"),
]
