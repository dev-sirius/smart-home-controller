
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index , name='index'),
    url(r'^temp', views.temp, name="temp"),
    url(r'^api/sensors', views.API, name="API"),
    url(r'^api/update', views.apiUpdate, name="apiUpdate"),
]
