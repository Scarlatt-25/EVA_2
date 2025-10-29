from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contacto

class ContactoListView(ListView):
    model = Contacto
    template_name = 'contactos/contacto_list.html'

class ContactoCreateView(CreateView):
    model = Contacto
    template_name = 'contactos/contacto_form.html'
    fields = ['nombre', 'telefono', 'email', 'notas']
    success_url = reverse_lazy('contactos:lista')

class ContactoUpdateView(UpdateView):
    model = Contacto
    template_name = 'contactos/contacto_form.html'
    fields = ['nombre', 'telefono', 'email', 'notas']
    success_url = reverse_lazy('contactos:lista')

class ContactoDeleteView(DeleteView):
    model = Contacto
    template_name = 'contactos/contacto_confirm_delete.html'
    success_url = reverse_lazy('contactos:lista')
