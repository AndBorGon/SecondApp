
from principal.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from principal.form import ContactoForm
from django.shortcuts import render_to_response,get_object_or_404
from SistReco.Sistemanuestro import *
from SistReco.recommendations import *
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
        cargar()
        rec = getRecommendations(puntuacionestotales,usuario.username)[0:2]
        print rec
    except :
        rec = None
    return render_to_response('verrecomendacion.html',{'rec':rec})


def recomendacion(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            return HttpResponseRedirect('/verrecomendacion')
    else:
        formulario = ContactoForm()
    return  render_to_response('recomendacion.html',{'formulario':formulario},context_instance=RequestContext(request))





