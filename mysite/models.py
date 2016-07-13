from django.db import models

class Arduinos(models.Model):
    name = models.CharField(max_length =50)
    crypto_key = models.CharField(max_length = 40)
    TYPE_CONNECTION = (
        'BLUETOOTH',
        'WIFI',
        'RADIO_433'
    )
    conn_type = models.CharField(max_length = 10,
    choices =  TYPE_CONNECTION,
    default = "WIFI")

    ip = models.GenericIPAdressField()
    port = models.IntegerField()

    name_bluetooth = models.CharField(max_length = 20)
    channel = models.IntegerField()
