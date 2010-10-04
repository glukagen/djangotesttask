# -*- coding: utf-8 -*-

from django import forms
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from base.context_processors import mysettings
from base.models import Person, PersonForm

def firstpage(request):
    p = Person.objects.get(pk=1)
    if request.method == 'POST':
        f = PersonForm(request.POST, instance=p)
        if f.is_valid():
            f.save()
    else:
        f = PersonForm(instance=p)
    c = {'form' : f, }
    c.update(csrf(request))
    return render_to_response("index.html", c)

def settings(request):
    return render_to_response('settings.html', {},
        context_instance=RequestContext(request, processors=[mysettings]))