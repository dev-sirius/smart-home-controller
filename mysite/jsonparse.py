import json
from . import Transport
from smarthouse.models import Arduino,Log,Sensors
from django.utils import timezone
import hashlib
from . import dbwork
import time
import RPi.GPIO as GPIO

isInitGPIO = True
transporter = Transport.TransportProtocol()

pin = 0
def verificate(request):
    json = request[32:]
    rhash = request[:32]
    MD5 = hashlib.md5()
    MD5.update(json.encode())
    chash = MD5.hexdigest()
    if rhash == chash:
        return json
    else:
        return None

def jsonExecute(text):

    try:
        etext = json.loads(text)
    except ValueError:
        return 'Packet is invalid'

    return etext

def set(text):
    etext = jsonExecute(text)
    try:
        Type = etext['type']
        global isInitGPIO
        if Type == 'LIGHT':
            try:
                light = int(etext['value'])
                if (isInitGPIO == True):
                    changeLight(light)
                else:
                    initGPIO()
                    isInitGPIO = True
                    changeLight(light)
                return 'Hooray!!!!'
            except KeyError:
                pass
    except KeyError:
        return 'Required argument (type) not found'

def registration(text):
    etext = jsonExecute(text)
    try:
        name_ard = etext['name_ard']
        key = etext['crypto_key']
        connection = etext['conn_type']
        if connection == 'wf':
            ip_ard = etext['ip']
            port_ard = etext['port']
            Arduino.objects.create(name=name_ard, crypto_key=key, conn_type=connection, ip=ip_ard, port=port_ard)
        elif connection == 'bt':
            blu_name = etext['blu_name']
            Arduino.objects.create(name=name_ard, crypto_key=key, conn_type=connection, name_bluetooth=blu_name)
        elif connection == 'rd':
            channel_radio = etext['channel_radio']
            Arduino.objects.create(name=name_ard, crypto_key=key, conn_type=connection, channel=channel_radio)
    except KeyError:
        pass
def update(text):
    etext = jsonExecute(text)
    try:
        Type = etext['type']

        if Type == 'TEMPERATURE':
            try:
                temperature = etext['value']
                id_a = etext['id']
                Log.objects.create(type=Type, id_arduino=id_a, value=temperature, date=timezone.now())

                return 'Hooray!!!!!'
            except KeyError:
                pass

        elif Type == 'LIGHT':
            try:
                light = etext['value']
                id_a = etext['id']
                Log.objects.create(type=Type, id_arduino=id_a, value=light, date=timezone.now())
                return 'Hooray!!!!?'
            except KeyError:
                pass
    except KeyError:
        return 'Required argument (type) not found'
def login(text):
    etext = jsonExecute(text)
    try:
        Type = etext['type']
        if Type == 'NEURON':
            isLogin = etext['is_login']
    except KeyError:
        pass
def changeLight(value):
    pin.ChangeDutyCycle(value*10)

def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    pin = GPIO.PWM(21, 200)
    pin.start(0)
    return True
