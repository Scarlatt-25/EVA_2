from django.contrib import admin
from .models import Contacto, Etiqueta

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'creado')
    list_filter = ('creado', 'etiquetas')
    search_fields = ('nombre', 'telefono', 'email')

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
