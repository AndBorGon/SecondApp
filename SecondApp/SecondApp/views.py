
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
    return render_to_response('usuario.html',{'users':users})

def verrecomendacion(request):

    dato = request.POST.get('user')
    try:
        usuario = Usuario.objects.get(username=dato)
        cargar()
        rec = getRecommendations(puntuacionestotales,usuario.username)[0:2]
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
    try:
        product = producto.objects.get(nombre=dato)
    except:
        product = None
    return render_to_response('verproducto.html',{'product':product})

def addusuario(request):
    if request.method == 'POST':
        formulariouser = AddUserForm(request.POST)
        if formulariouser.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            birth = request.POST.get('birth')
            Usuario.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,email=email,birth=birth)
            return HttpResponseRedirect('/addusuario')
    else:
        formulariouser = AddUserForm()
    return  render_to_response('addusuario.html',{'formulariouser':formulariouser},context_instance=RequestContext(request))
