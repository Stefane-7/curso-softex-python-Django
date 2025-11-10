from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tarefa, Execucao # 1. Importe o Model Tarefa
from .forms import TarefaForm

# Create your views here.
def home(request):
    # 3. Lógica de POST: Se o formulário foi enviado
    if request.method == 'POST':
        # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
        # 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
            # 5. Salva o objeto no banco de dados!
            form.save()
            # 6. Redireciona de volta para a 'home'
            # Isso é o Padrão "Post-Redirect-Get" (PRG)
            return redirect('home')
        # Se o form NÃO for válido, o código continua e
        # o 'form' (com os erros) será enviado para o template
        # 7. Lógica de GET: Se o usuário apenas visitou a página
    else:
        form = TarefaForm() # Cria um formulário vazio
        # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas
    execucao = Execucao.objects.all()
    # 9. Atualize o contexto para incluir o formulário
    context = {
    'nome_usuario': 'Algúem',
    'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
    'tarefas': todas_as_tarefas,
    'form': form, # 10. Envie o 'form' (vazio ou com erros) para o template
    'execucao': execucao
    }
    return render(request, 'home.html', context)

def home_2(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1>Olá, Mundo! Esta é minha segunda página Django!</h1>")
    
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'editar_tarefa.html', {'form': form, 'tarefa': tarefa})  

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('home')

def alternar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = not tarefa.concluida  # inverte o valor atual
    tarefa.save()
    return redirect('home')
  