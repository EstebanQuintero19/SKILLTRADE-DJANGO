from django.urls import path
from .views import (
    SkillListView,
    SkillDetailView,
    SkillCreateView,
    SkillUpdateView,
    SkillDeleteView
)

app_name = 'skilltrade_app'

urlpatterns = [
    path('', SkillListView.as_view(), name='skill_list'),
    path('<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    path('nuevo/', SkillCreateView.as_view(), name='skill_create'),
    path('<int:pk>/editar/', SkillUpdateView.as_view(), name='skill_update'),
    path('<int:pk>/eliminar/', SkillDeleteView.as_view(), name='skill_delete'),
] 