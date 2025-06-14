from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Curso

# Create your views here.

class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/curso_list.html'
    context_object_name = 'cursos'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/curso_detail.html'
    context_object_name = 'curso'

class CursoCreateView(CreateView):
    model = Curso
    template_name = 'cursos/curso_form.html'
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('cursos:curso_list')

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'cursos/curso_form.html'
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('cursos:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('cursos:curso_list')
