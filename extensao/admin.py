from django.contrib import admin
from .models import Categoria, Aluno, PerfilAcademico, Projeto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula')
    search_fields = ('nome', 'matricula')


class PerfilAcademicoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'link_lattes')
    search_fields = ('aluno__nome',)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_inicio')
    search_fields = ('titulo', 'descricao')
    list_filter = ('categoria', 'equipe')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(PerfilAcademico, PerfilAcademicoAdmin)
admin.site.register(Projeto, ProjetoAdmin)