from django.http import HttpResponse
from . import jsonparse
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
    elif request.method == 'POST':
        pass


def apiUpdate(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        jsonPost = request.POST['json']
        return HttpResponse(jsonparse.jsonExtecude(jsonPost))