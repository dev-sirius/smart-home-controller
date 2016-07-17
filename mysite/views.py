from django.http import HttpResponse
from . import jsonparse
from django.shortcuts import render_to_response
import os
from . import dbwork
from django.utils import timezone

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
    return render_to_response('index.html', {'temperature':int(dbwork.outOfDB('TEMPERATURE')), 'light':int(dbwork.outOfDB('LIGHT')) })

def API(request):
    if request.method == 'GET':
        resp = HttpResponse()
        resp.status_code = 405
        resp.write('Now method is not supported.')
        return resp
    
    elif request.method == 'POST':
        jsonPost = str(request.POST.get('data'))
        if jsonPost == None:
            resp = HttpResponse()
            resp.status_code = 406
            resp.write('Required argument not found.')
            return resp
    
        jsons = jsonparse.verificate(jsonPost)
        if jsons != None:
            return HttpResponse(jsonparse.jsonExecute(jsons))
        else:
            resp = HttpResponse()
            resp.status_code = 400
            resp.write('Are you trying hacking us?')
            return resp
        
    resp = HttpResponse()
    resp.status_code = 204
    resp.write('We need a request')
    return resp

def sendtime(request):
    return HttpResponse(str(timezone.now().time().hour+3) + ':' +
                        str(timezone.now().time().minute) + ':' +
                        str(timezone.now().time().second))
