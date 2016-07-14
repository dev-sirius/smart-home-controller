import json

G_Temperature = 10
G_Switch = True

text = input()

try:
    etext = json.loads(text)
except ValueError:
    print('Packet is invalid')

try:
    Method = etext['method']
except KeyError:
    print('Required argument (method) not found')

if Method == 'update':
    try:
        Type = etext['type']

        if Type == 'temperature':
            try:
                temperature = etext['temperature']
                G_Temperature = temperature
            except KeyError:
                pass

        elif Type == 'speed':
            try:
                switch = etext['switch']
                G_Switch = switch
            except KeyError:
                pass

    except KeyError:
        print('Required argument (type) not found')



