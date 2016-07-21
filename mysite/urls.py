
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^temp', views.temp, name="temp"),
    url(r'^api$', views.API, name="API"),
    url(r'^api/update', views.update, name="update"),
    url(r'^api/set', views.set, name="set"),
    url(r'^api/login', views.login, name="login"),
    url(r'^api/registration', views.registration, name="registration"),
    url(r'^time', views.sendtime, name="sendtime"),
    url(r'^camera', views.camera,name='camera')
]
