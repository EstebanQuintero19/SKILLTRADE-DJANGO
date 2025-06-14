from django.urls import path
from .views import (
    CursoListView,
    CursoDetailView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView
)

app_name = 'cursos'

urlpatterns = [
    path('', CursoListView.as_view(), name='curso_list'),
    path('<int:pk>/', CursoDetailView.as_view(), name='curso_detail'),
    path('nuevo/', CursoCreateView.as_view(), name='curso_create'),
    path('<int:pk>/editar/', CursoUpdateView.as_view(), name='curso_update'),
    path('<int:pk>/eliminar/', CursoDeleteView.as_view(), name='curso_delete'),
] 