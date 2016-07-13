from smarthouse.models import Arduino
from .Transport import TransportProtocol
import random

transporter = TransportProtocol()

def connectNewArduino(name, conn_type,ip=0, bluetooth_name=0, chanale = 0):
    private_key = random.randint(0,10**10)
    p = random.randint(0,10**10)
    g = random.randint(0,10**10)
    transporter.send(p,0,'WIFI')
    transporter.send(g, 0, 'WIFI')
    Akey = int((g**private_key) % p)
    transporter.send(Akey,0,'WIFI')
    Bkey = transporter.getPackageWIFI()
    crypto_key = (Bkey**private_key)%p
    ard = Arduino(name,crypto_key,conn_type,ip,bluetooth_name,chanale)
