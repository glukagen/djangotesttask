# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from base.models import Person
from django.template import RequestContext

from base.context_processors import mysettings

def firstpage(request):
    return render_to_response('index.html',
        {'object': get_object_or_404(Person, pk=1)})

def settings(request):
    return render_to_response('settings.html', {},
        context_instance=RequestContext(request, processors=[mysettings]))