from django.urls import path
from . import views # O '.' importa as 'views' do app atual

urlpatterns = [
# Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
    path('', views.home, name='home'),
    
    path('home_2/', views.home_2, name='home_2'), 
    
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'), 
    
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
   
    path('alternar/<int:id>/', views.alternar_tarefa, name='alternar_tarefa'),
    ]
