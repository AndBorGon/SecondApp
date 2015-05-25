__author__ = 'andres'
from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
    user = forms.CharField(max_length=30)
    #puntuacion = forms.CharField(max_length=30)
class ProductoForm(forms.Form):
    producto = forms.CharField(max_length=30)