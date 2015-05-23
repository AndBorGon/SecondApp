from django.shortcuts import render_to_response,get_object_or_404
from datetime import datetime
from principal.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from principal.form import ContactoForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response,get_object_or_404
import time
from datetime import date
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render_to_response('index.html')
def usuarios(request):
    users = Usuario.objects.all()
    print users
    return render_to_response('usuario.html',{'users':users})

def verrecomendacion(request):
    dato = request.POST.get('user')
    try:
        usuario = Usuario.objects.get(username=dato)
    except:
        usuario=""
    return render_to_response('verrecomendacion.html',{'usuario':usuario})


def recomendacion(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            return HttpResponseRedirect('/verrecomendacion')
    else:
        formulario = ContactoForm()
    return  render_to_response('recomendacion.html',{'formulario':formulario},context_instance=RequestContext(request))





