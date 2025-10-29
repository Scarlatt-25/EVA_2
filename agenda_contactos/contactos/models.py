from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, default='')
    email = models.EmailField(blank=True)
    notas = models.TextField(blank=True, default='')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
