# Create your models here.
#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
'''
class Usuario(models.Model):
    nick = models.ForeignKey(User, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='usuarios', verbose_name='imagen')
    def __unicode__(self):
        return self.nick
'''
class Tag(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
  
class Aplicacion(models.Model):
    TIPOS = (
    ('Animacion', 'Animacion'),
    ('Juego', 'Juego'),
    ('Otro', 'Otro'),
    )
    titulo = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=9, choices=TIPOS)
    tags = models.ManyToManyField(Tag, blank=True)
    codigo = models.TextField()
    sobre = models.TextField()
    imagen = models.ImageField(upload_to='aplicaciones', verbose_name='imagen')
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User) 
    def __unicode__(self):
        return self.titulo
