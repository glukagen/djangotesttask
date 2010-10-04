# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from base.models import Person

def firstpage(request):
    return render_to_response('index.html',
        {'object': get_object_or_404(Person, pk=1)})
