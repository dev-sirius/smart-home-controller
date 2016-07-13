from django.http import HttpResponse
from django.shortcuts import render_to_response
import os

class TransportProtocol:
	def send(packet, key, connection_info):
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
		# return AES_encode
	def AES_decode(spacket, key):
		# return AES_decode

	def encode(packet, key):
		return self.AES_encode(packet, key)
	def decode(spacket, key):
		return self.AES_decode(spacket, key)

	# send to sensors using Wi-Fi
	def sendWIFI(spacket, connection_info):
		ip = connection_info.name
		#...
	# send to sensors using BLUETOOTH
	def sendBLUETOOTH(spacket, connection_info):
		name = connection_info.name
		#...
	# send to sensors using 433
	def send433(spacket, connection_info):
		#..
def index(request):
    try:
        temp = request.GET['temperature']
        return render_to_response('index.html', {'temperature' : temp})
    except KeyError:
        resp = HttpResponse()
        resp.status_code = 406
        resp.write('Required argument not found.')
        return resp

def API(request):
	if request.method == 'GET':
		pass
		#do()
	elif request.method == 'POST':
		pass
		#do2()
