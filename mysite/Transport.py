class TransportProtocol:
    def send(self, packet, key, connection_info):
        # encode packet for send
        spacket = self.encode(packet, key)
        # choose type of connection
        if connection_info.type == 'WIFI':
            self.sendWIFI(spacket, connection_info)
        elif connection_info.type == 'BLUETOOTH':
            self.sendBLUETOOTH(spacket, connection_info)
        elif connection_info.type == '433':
            self.send433(spacket, connection_info)

    def AES_encode(packet, key):
        pass

    # return AES_encode
    def AES_decode(spacket, key):
        pass

    # return AES_decode

    def encode(self, packet, key):
        return self.AES_encode(packet, key)

    def decode(self, spacket, key):
        return self.AES_decode(spacket, key)

    # send to sensors using Wi-Fi
    def sendWIFI(spacket, connection_info):
        ip = connection_info.name

    # ...
    # send to sensors using BLUETOOTH
    def sendBLUETOOTH(spacket, connection_info):
        name = connection_info.name

    # ...
    # send to sensors using 433
    def send433(spacket, connection_info):
        pass


    def getPackageWIFI(self):
        arduino_name = ''
        package = 0
        return (arduino_name, package)
