from django.urls import path
from .views import ListaTarefasAPIView, TarefasEstatisticasAPIView, DetalheTarefaAPIView, DuplicarTarefaAPIView, ConcluirTodasTarefasAPIView, LogoutView 
from .views import MinhaView, ChangePasswordView
app_name = 'core'
urlpatterns = [

    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/estatisticas/', TarefasEstatisticasAPIView.as_view()),
    path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('me/', MinhaView.as_view(), name='teste-autenticado'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'), 
]
