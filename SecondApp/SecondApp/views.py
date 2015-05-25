
from principal.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from principal.form import *
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
    #puntuacion = request.POST.get('puntuacion')
    try:
        usuario = Usuario.objects.get(username=dato)
        #usuariover=Usuario.objects.get(username=puntuacion)
        cargar()
        rec = getRecommendations(puntuacionestotales,usuario.username)[0:2]
        #print usuario
    except :
        rec = None
        #usuariover = None
    return render_to_response('verrecomendacion.html',{'rec':rec})


def recomendacion(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            return HttpResponseRedirect('/verrecomendacion')
    else:
        formulario = ContactoForm()
    return render_to_response('recomendacion.html',{'formulario':formulario},context_instance=RequestContext(request))

def productos(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            return HttpResponseRedirect('/verproducto')
    else:
        formulario = ProductoForm()
    return  render_to_response('producto.html',{'formulario':formulario},context_instance=RequestContext(request))

def verproducto(request):
    dato = request.POST.get('producto')
    product = producto.objects.get(nombre=dato)
    #product = producto.objects.get(nombre=dato)
    #print product.tienda_that_belongs.all()
    return render_to_response('verproducto.html',{'product':product})


