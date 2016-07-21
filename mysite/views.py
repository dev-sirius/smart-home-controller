from django.http import HttpResponse
from . import jsonparse
from django.shortcuts import render_to_response
import os
from . import dbwork
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {'temperature':int(dbwork.outOfDB('TEMPERATURE')), 'light':int(dbwork.outOfDB('LIGHT')) })
    else:
        return HttpResponseRedirect('https://192.168.1.1/login')

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
def set(request):
    if request.method == 'POST':
        jsonPost = str(request.POST.get('data'))
        if jsonPost == None:
            resp = HttpResponse()
            resp.status_code = 406
            resp.write('Required argument not found.')
            return resp
        jsons = jsonparse.verificate(jsonPost)
        if jsons != None:
            return HttpResponse(jsonparse.set(jsons))
        else:
            resp = HttpResponse()
            resp.status_code = 400
            resp.write('Are you trying hacking us?')
            return resp
def update(request):
    if request.method == 'POST':
        jsonPost = str(request.POST.get('data'))
        return HttpResponse(jsonparse.verificate(jsonPost))
        '''if jsonPost == None:
            resp = HttpResponse()
            resp.status_code = 406
            resp.write('Required argument not found.')
            return resp
        jsons = jsonparse.verificate(jsonPost)
        if jsons != None:
            return HttpResponse(jsonparse.update(jsons))
        else:
            resp = HttpResponse()
            resp.status_code = 400
            resp.write('Are you trying hacking us?')
            return resp'''

def registration(request):
    if request.method == 'POST':
        jsonPost = str(request.POST.get('data'))
        if jsonPost == None:
            resp = HttpResponse()
            resp.status_code = 406
            resp.write('Required argument not found.')
            return resp
        jsons = jsonparse.verificate(jsonPost)
        if jsons != None:
            return HttpResponse(jsonparse.registration(jsons))
        else:
            resp = HttpResponse()
            resp.status_code = 400
            resp.write('Are you trying hacking us?')
            return resp
def sendtime(request):
    return HttpResponse(str(timezone.now().time().hour+3) + ':' +
                        str(timezone.now().time().minute) + ':' +
                        str(timezone.now().time().second))
def camera(request):
    return render_to_response("Camera.html",{})

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        passwd = request.POST.get('pass')
        user = authenticate(username = name, password = passwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('https://192.168.1.1/')
            else:
                return HttpResponse('user is not active')
        else:
                return HttpResponse('login or password is invalid')

    elif request.method == 'GET':
        return render_to_response('login.html',{})

