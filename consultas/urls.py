from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_consultas, name='lista_consultas'),
    path('criar/', views.criar_consulta, name='criar_consulta'),
    path('editar/<int:id>/', views.editar_consulta, name='editar_consulta'),
    path('excluir/<int:id>/', views.excluir_consulta, name='excluir_consulta'),
]