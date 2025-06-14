from django.urls import path
from .views import (
    IntercambioListView,
    IntercambioDetailView,
    IntercambioCreateView,
    IntercambioUpdateView,
    IntercambioDeleteView
)

app_name = 'intercambios'

urlpatterns = [
    path('', IntercambioListView.as_view(), name='intercambio_list'),
    path('<int:pk>/', IntercambioDetailView.as_view(), name='intercambio_detail'),
    path('nuevo/', IntercambioCreateView.as_view(), name='intercambio_create'),
    path('<int:pk>/editar/', IntercambioUpdateView.as_view(), name='intercambio_update'),
    path('<int:pk>/eliminar/', IntercambioDeleteView.as_view(), name='intercambio_delete'),
] 