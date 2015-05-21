__author__ = 'andres'
from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
    user = forms.CharField(widget=forms.Textarea)