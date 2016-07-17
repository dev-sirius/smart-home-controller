
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^temp', views.temp, name="temp"),
    url(r'^api', views.API, name="API"),
    url(r'^time', views.sendtime, name="sendtime"),
]
