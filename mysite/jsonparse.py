import json
from . import Transport
from smarthouse.models import Arduino,Log
from django.utils import timezone
import hashlib

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
    transporter = Transport.TransportProtocol()

    try:
        etext = json.loads(text)
    except ValueError:
        return 'Packet is invalid'

    try:
        Method = etext['method']
    except KeyError:
        return 'Required argument (method) not found'

    if Method == 'UPDATE':
        try:
            Type = etext['type']

            if Type == 'TEMPERATURE':
                try:
                    temperature = etext['temperature']
                    id_a = etext['id']
                    Log.objects.create(type = Type,id_arduino = id_a,value =temperature,date = timezone.now())
                    return 'Hooray!!!!!'
                except KeyError:
                    pass

            elif Type == 'LIGHT':
                try:
                    light = etext['light_switch']
                    id_a = etext['id']
                    Log.objects.create(type=Type, id_arduino=id_a, value=light, date=timezone.now())
                    return 'Hooray!!!!!'
                except KeyError:
                    pass
        except KeyError:
            return 'Required argument (type) not found'

    if Method == 'LOGIN':
        try:
            Type = etext['type']
            if Type == 'NEURON':
                isLogin = etext['is_login']
        except KeyError:
            pass