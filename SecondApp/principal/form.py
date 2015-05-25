__author__ = 'andres'
from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
    user = forms.CharField(max_length=30)
    #puntuacion = forms.CharField(max_length=30)
class ProductoForm(forms.Form):
    producto = forms.CharField(max_length=30)

class AddUserForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=15)
    email =  forms.EmailField()
    password = forms.CharField(max_length=15)
    birth = forms.DateField()