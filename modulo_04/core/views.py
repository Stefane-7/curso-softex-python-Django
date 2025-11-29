from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login 
from .models import Tarefa
from .forms import TarefaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    # 3. Lógica de POST: Se o formulário foi enviado
    if request.method == 'POST':
        # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST, user=request.user)
        if form.is_valid():
            
            tarefa = form.save(commit=False)
            tarefa.user = request.user
            tarefa.save()
            return redirect('home')
    else:
       form = TarefaForm(user=request.user) 

    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')
    context = {
    'nome_usuario':  request.user.username,
    'tecnologias': ['Autenticação', 'ForeignKey', 'Login'],
    'tarefas': todas_as_tarefas,
    'form': form,
    }
    return render(request, 'home.html', context)

@login_required    
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'editar_tarefa.html', {'form': form, 'tarefa': tarefa})  

@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    tarefa.delete()
    return redirect('home')

@login_required
def alternar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    tarefa.concluida = not tarefa.concluida  # inverte o valor atual
    tarefa.save()
    return redirect('home')

def register(request):
    # Se a requisição for POST, o usuário enviou o formulário
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = UserCreationForm(request.POST)
        # Verifica se o formulário é válido (ex: senhas batem, username não existe)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco
            login(request, user) # Faz o login automático do usuário
            return redirect('home') # Redireciona para a home

    else:
        form = UserCreationForm() # Cria um formulário de cadastro vazio

        # Prepara o contexto e renderiza o template
        context = {'form': form}
        return render(request, 'register.html', context)