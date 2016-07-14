from django.http import HttpResponse
from django.shortcuts import render_to_response
import os


def temp(request):
	try:
		temp = request.GET['temperature']
		return render_to_response('temp.html', {'temperature': temp})
	except KeyError:
		resp = HttpResponse()
		resp.status_code = 406
		resp.write('Required argument not found.')
		return resp

def index(request):
	return render_to_response('index.html', {})

def API(request):
	if request.method == 'GET':
		pass
		#do()
	elif request.method == 'POST':
		pass
		#do2()
