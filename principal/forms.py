#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Aplicacion,Tag

class AplicacionForm(ModelForm):
    class Meta:
        model = Aplicacion
        #exclude = ('usuario')

class MetaForm(ModelForm):
    class Meta:
        model = Tag
        