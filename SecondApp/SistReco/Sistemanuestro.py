__author__ = 'javier'
from django.db import models
from principal.models import *
puntuacionestotales=None
def cargar():
    puntuaciones={'baja':1,'bajo-medio':2,'medio':3,'medio-alto':4,'alto':5}
    productosmap={}
    puntuacion={}
    todosusuarios = Usuario.objects.all()
    for usuario in todosusuarios:
        productosmap[usuario]={}
        for pro in usuario.puntuacionesProducto.all():
            productosmap[usuario].update({pro.__str__() : puntuaciones.get(clasificationproducto.objects.get(producto=pro,usuario_pd_fk=usuario).__str__())})
        puntuacion.update({usuario.username: productosmap[usuario]})
    globals()['puntuacionestotales']= puntuacion
    #print "Sistema De Recomendacion Cargada/Actualizada"
