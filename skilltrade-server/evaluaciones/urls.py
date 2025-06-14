from django.urls import path
from .views import (
    EvaluacionListView,
    EvaluacionDetailView,
    EvaluacionCreateView,
    EvaluacionUpdateView,
    EvaluacionDeleteView
)

app_name = 'evaluaciones'

urlpatterns = [
    path('', EvaluacionListView.as_view(), name='evaluacion_list'),
    path('nueva/', EvaluacionCreateView.as_view(), name='evaluacion_create'),
    path('<int:pk>/', EvaluacionDetailView.as_view(), name='evaluacion_detail'),
    path('<int:pk>/editar/', EvaluacionUpdateView.as_view(), name='evaluacion_update'),
    path('<int:pk>/eliminar/', EvaluacionDeleteView.as_view(), name='evaluacion_delete'),
] 