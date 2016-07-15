from django.http import HttpResponse
from . import jsonparse
from django.shortcuts import render_to_response
import os
from . import dbwork

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
    return render_to_response('index.html', {'temperature':dbwork.outOfDB('TEMPERATURE'),'is_light':str(dbwork.outOfDB('LIGHT').lower())})

def API(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        jsonPost = str(request.POST.get('data'))
        jsons = jsonparse.verificate(jsonPost)
        if jsons != None:
            return HttpResponse(jsonparse.jsonExecute(jsons))
        else:
            return HttpResponse('Request is corrupted')
    return HttpResponse('<h1>We need a request</h1>')

