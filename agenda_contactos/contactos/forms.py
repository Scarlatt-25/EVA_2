# contactos/forms.py
from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'email']

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        # Quitamos espacios para contar solo los números
        solo_numeros = telefono.replace(" ", "")
        if len(solo_numeros) > 9:
            raise forms.ValidationError("El teléfono no puede tener más de 9 dígitos")
        if not re.fullmatch(r'[\d\s]+', telefono):
            raise forms.ValidationError("El teléfono solo puede contener números y espacios")
        return telefono

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Ingresa un correo electrónico válido")
        return email
