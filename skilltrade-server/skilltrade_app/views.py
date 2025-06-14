from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Skill

# Create your views here.

class SkillListView(ListView):
    model = Skill
    template_name = 'skilltrade_app/skill_list.html'
    context_object_name = 'skills'

class SkillDetailView(DetailView):
    model = Skill
    template_name = 'skilltrade_app/skill_detail.html'
    context_object_name = 'skill'

class SkillCreateView(CreateView):
    model = Skill
    template_name = 'skilltrade_app/skill_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('skilltrade_app:skill_list')

class SkillUpdateView(UpdateView):
    model = Skill
    template_name = 'skilltrade_app/skill_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('skilltrade_app:skill_list')

class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'skilltrade_app/skill_confirm_delete.html'
    success_url = reverse_lazy('skilltrade_app:skill_list')
