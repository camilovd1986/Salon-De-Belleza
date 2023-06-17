from django.db import models
from enum import Enum

# Create your models here.


class Cita(models.Model):
    class Tipo_identidad(models.TextChoices):
        CEDULA = "CEDULA",
        TARJETA_IDENTIDAD = "IDENTIDAD",
        REGISTRO_CIVIL = "CIVIL",

    class Tipo_servicio(models.TextChoices):
        BARBERIA = "BARBERIA",
        MASAJES = "MASAJES",
        PELUQUERIA = "PELUQUERIA",
        FACIAL = "FACIAL",
        UNAS = "UNAS",

    nombre = models.CharField(
        max_length=100, blank=False, verbose_name='Nombre completo')
    tipo_identificacion = models.CharField(
        max_length=100, choices=Tipo_identidad.choices, default=Tipo_identidad.CEDULA)
    numero_identificacion = models.IntegerField(
        blank=True, verbose_name='Numero de identificacion')
    telefono = models.IntegerField(
        blank=False, verbose_name='Numero de telefono')
    direccion = models.CharField(
        max_length=100, blank=True, verbose_name='Direccion')
    email = models.EmailField(
        max_length=100, blank=True, verbose_name='Direccion de correo electronico')
    servicio = models.CharField(
        max_length=100, choices=Tipo_servicio.choices, default=Tipo_servicio.BARBERIA)
    profesional = models.CharField(
        max_length=100, blank=True, verbose_name='Profesional')
    fecha = models.DateField(max_length=100, blank=False,
                             verbose_name='Fecha del servicio')
    hora = models.TimeField(max_length=100, blank=False,
                            verbose_name='Hora del servicio')

    def __str__(self):
        return self.nombre
