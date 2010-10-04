# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from base.context_processors import mysettings
from base.models import Person, PersonForm

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

@csrf_protect
def firstpage(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    p = Person.objects.get(pk=1)
    if request.method == 'POST':
        f = PersonForm(request.POST, instance=p)
        if f.is_valid():
            f.save()
    else:
        f = PersonForm(instance=p)

    return render_to_response("index.html", {'form' : f, },
        context_instance=RequestContext(request))

def settings(request):
    return render_to_response('settings.html', {},
        context_instance=RequestContext(request, processors=[mysettings]))