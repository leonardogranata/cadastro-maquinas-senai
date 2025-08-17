from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerenciadorMaquinas, name='gerenciadorMaquinas'),
    path('cadastrar/colaborador/', views.cadastrarColaborador, name='cadastrarColaborador'),
    path('cadastrar/maquina/', views.cadastrarMaquina, name='cadastrarMaquina'),
    path('editar/maquina/<int:pk>/', views.editarMaquina, name='editarMaquina'),
    path('excluir/maquina/<int:pk>/', views.excluirMaquina, name='excluirMaquina'),
]
