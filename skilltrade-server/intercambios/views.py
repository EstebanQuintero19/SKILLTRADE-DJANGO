from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Intercambio

# Create your views here.

class IntercambioListView(ListView):
    model = Intercambio
    template_name = 'intercambios/intercambio_list.html'
    context_object_name = 'intercambios'

class IntercambioDetailView(DetailView):
    model = Intercambio
    template_name = 'intercambios/intercambio_detail.html'
    context_object_name = 'intercambio'

class IntercambioCreateView(CreateView):
    model = Intercambio
    template_name = 'intercambios/intercambio_form.html'
    fields = ['titulo', 'descripcion', 'aceptado']
    success_url = reverse_lazy('intercambios:intercambio_list')

class IntercambioUpdateView(UpdateView):
    model = Intercambio
    template_name = 'intercambios/intercambio_form.html'
    fields = ['titulo', 'descripcion', 'aceptado']
    success_url = reverse_lazy('intercambios:intercambio_list')

class IntercambioDeleteView(DeleteView):
    model = Intercambio
    template_name = 'intercambios/intercambio_confirm_delete.html'
    success_url = reverse_lazy('intercambios:intercambio_list')
