# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
import json

from base.context_processors import mysettings
from base.models import Person, PersonForm, Location

@csrf_protect
def mylogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                        password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Disabled account'
        else:
            error = 'Invalid login'
    else:
        error = ''
    return render_to_response("login.html", {'error' : error},
        context_instance=RequestContext(request))

def firstpage(request):    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    p = Person.objects.get(pk=1)
    f = PersonForm(instance=p)
    labels = []
    for field in f:
        labels.append(field)
    labels.reverse()
    
    return render_to_response("index.html", {'form' : labels, 'user' : p},
        context_instance=RequestContext(request))

def save_person(request):
    if not request.user.is_authenticated():
        return HttpResponse('You are not authorized')        
    if not request.is_ajax:
        return HttpResponse('Should be ajax request')
    if request.method != 'POST':
        return HttpResponse('Should be POST request')
        
    f = PersonForm(request.POST, instance=Person.objects.get(pk=1))
    if f.is_valid():
        f.save()
        return HttpResponse('1') 
    else:        
        return HttpResponse(json.dumps({'errors':f.errors}))
        
def settings(request):
    return render_to_response('settings.html', {},
        context_instance=RequestContext(request, processors=[mysettings]))
    

def middleware(request):
    return render_to_response('middleware.html',
        { 'location': Location.objects.all()[:10]},
        context_instance=RequestContext(request))

    