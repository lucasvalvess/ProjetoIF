from django.db import models

class Categoria(models.Model):

    nome = models.CharField(max_length=100)

    def __str__(self): 
        return self.nome

class Aluno(models.Model):

    nome = models.CharField(max_length=100)

    matricula = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class PerfilAcademico(models.Model): 

    link_lattes = models.URLField()

    biografia = models.TextField()

    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.nome

class Projeto(models.Model): 

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='projetos')

    equipe = models.ManyToManyField(Aluno, related_name='projetos')

    def __str__(self):
        return self.titulo 



