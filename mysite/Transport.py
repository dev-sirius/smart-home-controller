class TransportProtocol:
    def send(self, packet, arduino):
        # encode packet for send
        #spacket = self.encode(packet, key)
        # choose type of connection
        if arduino.conn_type == 'wf':
            self.sendWIFI(packet, arduino)
        elif arduino.conn_type == 'bt':
            self.sendBLUETOOTH(packet, arduino)
        elif arduino.conn_type == 'rd':
            self.send433(packet, arduino)

    '''def AES_encode(packet, key):
        pass

    # return AES_encode
    def AES_decode(spacket, key):
        pass

    # return AES_decode

    def encode(self, packet, key):
        return self.AES_encode(packet, key)

    def decode(self, spacket, key):
        return self.AES_decode(spacket, key)
    '''
    # send to sensors using Wi-Fi
    def sendWIFI(package, arduino):
        ip = arduino.ip

    # ...
    # send to sensors using BLUETOOTH
    def sendBLUETOOTH(package, arduino):
        name = arduino.name_bluetooth

    # ...
    # send to sensors using 433
    def send433(package, arduino):
        pass


    def getPackageWIFI(self):
        arduino_name = ''
        package = 0
        return (arduino_name, package)
