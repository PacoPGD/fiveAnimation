# Create your views here.
#Importo las clases
from principal.models import *
#Importo los formularios
from principal.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
 
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        tagis = Tag.objects.filter(nombre__icontains=q)
        aplicaciones = (Aplicacion.objects.filter(titulo__icontains=q) | Aplicacion.objects.filter(tags=tagis)).distinct()     
        return render_to_response('resultadoBusqueda.html', {'aplicaciones': aplicaciones, 'query': q},context_instance=RequestContext(request))
    else:
        return render_to_response('mensaje.html',{'mensaje':'No se ha encontrado nada'},context_instance=RequestContext(request)) 

def index(request):
    aplicaciones = Aplicacion.objects.all()
    return render_to_response('index.html',{'aplicaciones':aplicaciones},context_instance=RequestContext(request))

def animaciones(request):
    aplicaciones = Aplicacion.objects.all()
    return render_to_response('animaciones.html',{'aplicaciones':aplicaciones},context_instance=RequestContext(request))

def juegos(request):
    aplicaciones = Aplicacion.objects.all()
    return render_to_response('juegos.html',{'aplicaciones':aplicaciones},context_instance=RequestContext(request))

def otros(request):
    aplicaciones = Aplicacion.objects.all()
    return render_to_response('otros.html',{'aplicaciones':aplicaciones},context_instance=RequestContext(request))

def sobre(request):
    return render_to_response('sobre.html',context_instance=RequestContext(request))

def runapp(request, ide):
    aplicaciones = Aplicacion.objects.all()
    ide = int(ide)
    return render_to_response('runapp.html',{'aplicaciones':aplicaciones,'ide':ide},context_instance=RequestContext(request))

def nuevaApp(request):
    formulario=AplicacionForm(request.POST, request.FILES)
    metas = Tag.objects.all()
    if formulario.is_valid():
        formulario.save()
        return render_to_response('mensaje.html',{'mensaje':'Aplicacion subida'},context_instance=RequestContext(request))        
    return render_to_response('nuevaApp.html',{'formulario':formulario,'metas':metas}, context_instance=RequestContext(request))

def nuevoTag(request):
    formulario=MetaForm(request.POST, request.FILES)
    if formulario.is_valid():
        formulario.save()
        return render_to_response('mensaje.html',{'mensaje':'Tag registrado'},context_instance=RequestContext(request))        
    return render_to_response('nuevoTag.html',{'formulario':formulario}, context_instance=RequestContext(request))

def registro(request):
    formulario = UserCreationForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/')
    return render_to_response('registro.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('mensaje.html',{'mensaje':'no activo'},context_instance=RequestContext(request)) 
            else:
                return render_to_response('mensaje.html',{'mensaje':'password o usuario incorrecto'},context_instance=RequestContext(request)) 
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
