from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Section

def minipressroom(request):
    
    return render_to_response("minipressroom/pressroom.html",dict(sections=Section.get_all()),context_instance=RequestContext(request))
