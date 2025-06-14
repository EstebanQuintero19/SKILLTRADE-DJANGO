from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evaluacion

# Create your views here.

class EvaluacionListView(ListView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_list.html'
    context_object_name = 'evaluaciones'

class EvaluacionDetailView(DetailView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_detail.html'
    context_object_name = 'evaluacion'

class EvaluacionCreateView(CreateView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_form.html'
    fields = ['titulo', 'comentario', 'puntuacion']
    success_url = reverse_lazy('evaluaciones:evaluacion_list')

class EvaluacionUpdateView(UpdateView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_form.html'
    fields = ['titulo', 'comentario', 'puntuacion']
    success_url = reverse_lazy('evaluaciones:evaluacion_list')

class EvaluacionDeleteView(DeleteView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_confirm_delete.html'
    success_url = reverse_lazy('evaluaciones:evaluacion_list')
