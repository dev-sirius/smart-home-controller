from django.db import models
from django.utils import timezone

class Arduino(models.Model):
    name = models.CharField(max_length=50)
    crypto_key = models.CharField(max_length=40)

    TYPE_CONNECTION = (
        ('bl', 'BLUETOOTH'),
        ('wf', 'WIFI'),
        ('rd', 'RADIO_433')
    )
    conn_type = models.CharField(max_length=2,
                                 choices=TYPE_CONNECTION,
                                 default="wf")

    ip = models.GenericIPAddressField()
    port = models.IntegerField()

    name_bluetooth = models.CharField(max_length=20)
    channel = models.IntegerField()

class log(models.Model):
    type = models.CharField(max_length=50)
    id_arduino = models.IntegerField()
    value = models.FloatField()
    date = models.DateField()

    def saveRecord(self):
        self.date = timezone.now()
        self.save()