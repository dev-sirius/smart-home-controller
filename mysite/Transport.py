import hashlib

class TransportProtocol:
    def send(self, packet,packet_type, arduino):
        # encode packet for send
        spacket = self.encode(packet,packet_type, arduino.crypto_key)
        # choose type of connection
        if arduino.conn_type == 'wf':
            self.sendWIFI(spacket, arduino)
        elif arduino.conn_type == 'bt':
            self.sendBLUETOOTH(spacket, arduino)
        elif arduino.conn_type == 'rd':
            self.send433(spacket, arduino)

    def AES_encode(spacket, key):
        return spacket

    # return AES_encode
    def AES_decode(spacket, key):
        return spacket

    # return AES_decode

    def encode(self, packet, packet_type, key):
        json_query = '{"method":"SET"'+packet_type+',"value":'+packet+'}'
        aes_json = self.AES_encode(json_query, key)
        MD5 = hashlib.md5()
        MD5.update(aes_json.encode())
        chash = MD5.hexdigest()
        aes_json = chash + aes_json
        return aes_json

    def decode(self, spacket, key):
        return self.AES_decode(spacket, key)

    # send to sensors using Wi-Fi
    def sendWIFI(package, arduino):
        ip = arduino.ip
        port = arduino.port

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
