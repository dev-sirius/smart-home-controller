from smarthouse.models import Arduino
from .Transport import TransportProtocol
import random

transporter = TransportProtocol()

def connectNewArduino(name, conn_type,p,g,Bkey,ip=0, bluetooth_name=0, chanale = 0):
    private_key = random.randint(0,10**10)

    transporter.send(p,0,conn_type)
    transporter.send(g, 0, conn_type)
    Akey = int((g**private_key) % p)
    transporter.send(Akey,0,conn_type)
    crypto_key = (Bkey**private_key)%p
    Arduino.objects.create(name,crypto_key,conn_type,ip,bluetooth_name,chanale)
