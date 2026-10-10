from django.urls import path
from . import views

app_name = 'extensao'

urlpatterns = [

    path('', views.listagem_projeto, name='listaProjetos'),
    path('projetos/<int:id>/', views.detalhes_projeto, name='detalhesProjeto'),
    path('alunos/<int:id>/', views.detalhes_aluno, name='detalhesAluno'),
]