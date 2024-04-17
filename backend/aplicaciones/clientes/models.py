from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False, default='')
    apellido_paterno = models.CharField(max_length=60, blank=False, null=False, default='')
    apellido_materno = models.CharField(max_length=60, blank=False, null=False, default='')
    correo = models.EmailField()
    telefono = models.CharField(max_length=9, blank=False, null=False, default='')
    fecha_dominio = models.DateField()
    fecha_hosting = models.DateField()
    link_pagina_web = models.CharField(max_length=250, blank=False, null=False, default='')
