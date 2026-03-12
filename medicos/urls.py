from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicos, name='lista_medicos'),
    path('novo/', views.novo_medico, name='novo_medico'),
    path('editar/<int:id>/', views.editar_medico, name='editar_medico'),
    path('excluir/<int:id>/', views.excluir_medico, name='excluir_medico'),
]