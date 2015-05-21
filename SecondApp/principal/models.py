from django.db import models
from django.contrib.auth.models import User

class tienda(models.Model):
    nombre = models.CharField(max_length=30)
    url = models.URLField()
    email = models.EmailField()
    def __unicode__(self):
        return self.nombre +" "+ self.url

class precio(models.Model):
    cantidad = models.IntegerField()
    producto_fk=models.ForeignKey('producto')
    tienda_fk=models.ForeignKey('tienda')
    def __unicode__(self):
        return self.cantidad.__str__()

class producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)
    categoria = models.CharField(choices=(('Ebook','Ebook'),('Cd','Cd'),('Dvd','Dvd')),max_length=30)
    tienda_that_belongs = models.ManyToManyField(tienda,through=precio)
    def __unicode__(self):
        return self.nombre

class clasificationproducto(models.Model):
    puntuaciones=(('baja',1),('bajo-medio',2),('medio',3),('medio-alto',4),('alto',5))
    puntuaction=models.CharField(choices=puntuaciones,default='medio',max_length=30)
    producto=models.ForeignKey('producto')
    usuario_pd_fk=models.ForeignKey('Usuario')
    def __unicode__(self):
        return self.puntuaction

class clasificationtienda(models.Model):
    puntuaciones=(('baja',1),('bajo-medio',2),('medio',3),('medio-alto',4),('alto',5))
    puntuaction=models.CharField(choices=puntuaciones,default='medio',max_length=30)
    tienda_fk=models.ForeignKey('tienda')
    usuario_ti_fk=models.ForeignKey('Usuario')
    def __unicode__(self):
        return self.puntuaction

class Usuario(User):
    birth=models.DateField()
    puntuacionesTienda =  models.ManyToManyField(tienda,through=clasificationtienda)
    puntuacionesProducto =  models.ManyToManyField(producto,through=clasificationproducto)
    def __unicode__(self):
        return self.username

