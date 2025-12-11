from django.urls import path
from .views import ListaTarefasAPIView, TarefasEstatisticasAPIView, DetalheTarefaAPIView, DuplicarTarefaAPIView, ConcluirTodasTarefasAPIView

app_name = 'core'
urlpatterns = [

    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/estatisticas/', TarefasEstatisticasAPIView.as_view()),
    path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
]
