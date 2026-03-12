from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_paciente, name='lista_pacientes'),
    path('novo/', views.criar_paciente, name='criar_paciente'),
    path('editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('excluir/<int:id>/', views.excluir_paciente, name='excluir_paciente'),
    
]