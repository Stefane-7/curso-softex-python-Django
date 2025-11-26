from django.contrib import admin
from .models import Tarefa # 1. Importe seu Model
# Register your models here.
class TarefaAdmin(admin.ModelAdmin):
    # 'list_display' é uma tupla com os nomes dos campos
    # que queremos exibir como colunas na lista
    list_display = ('titulo', 'user', 'concluida', 'criada_em')

    # - 'concluida': Filtro de "Sim/Não"
    # - 'user': Filtro de lista (baseado em um ForeignKey)
    # - 'criada_em': Filtro de data (Hoje, Últimos 7 dias, Este mês, etc.)
    list_filter = ('concluida', 'user', 'criada_em')

admin.site.register(Tarefa, TarefaAdmin)
