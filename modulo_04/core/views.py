from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa # 1. Importe o Model Tarefa
# Create your views here.
def home(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    # 2. Use o ORM para buscar os dados!
    # Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa"
    todas_as_tarefas = Tarefa.objects.all()

    context = {
        'nome_usuario': 'alguém',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas # 4. Adicione as tarefas ao contexto
    }
    return render(request, 'home.html', context)

def home_2(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1>Olá, Mundo! Esta é minha segunda página Django!</h1>")
    