from django.shortcuts import render

from .models import Projeto, Aluno

def listagem_projeto(request):

    context = {'projetos': Projeto.objects.all()}

    return render(request, 'extensao/listagem_projetos.html', context)

def detalhes_projeto(request, id):

    projeto = Projeto.objects.get(id=id)

    context = {'projeto': projeto}

    return render(request, 'extensao/detalhes_projeto.html', context)

def detalhes_aluno(request, id):

    aluno = Aluno.objects.get(id=id)

    context = {'aluno': aluno}
    
    return render(request, 'extensao/detalhes_aluno.html', context)