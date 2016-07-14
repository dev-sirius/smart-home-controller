import json

def jsonExtecude(text):
    G_Temperature = 10
    G_Switch = True

    try:
        etext = json.loads(text)
    except ValueError:
        print('Packet is invalid')

    try:
        Method = etext['method']
    except KeyError:
        print('Required argument (method) not found')

    if Method == 'UPDATE':
        try:
            Type = etext['type']

            if Type == 'TEMPERATURE':
                try:
                    temperature = etext['temperature']
                    G_Temperature = temperature
                    return G_Temperature
                except KeyError:
                    pass

            elif Type == 'SPEED':
                try:
                    switch = etext['switch']
                    G_Switch = switch
                except KeyError:
                    pass

        except KeyError:
            print('Required argument (type) not found')



