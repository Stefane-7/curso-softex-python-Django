from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tarefa(models.Model):

    PRIORIDADE_CHOICES = [
    ('baixa', 'Baixa'),
    ('media', 'Média'),
    ('alta', 'Alta'),
]

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
        verbose_name='Prioridade'
    )

    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tarefas',  # Permite user.tarefas.all()
        verbose_name='Usuário'
    )
    # CharField: Campo de texto com limite
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )

    concluida = models.BooleanField(
        default=False,
        verbose_name='Concluída'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em'
    )

    prazo = models.DateField(
        null=True,
        blank=True,
        verbose_name='Prazo'
    )
    
    data_conclusao = models.DateField(
        null=True, 
        blank=True,
        verbose_name= 'Data de Conclusão'
    )

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']  # Mais recentes primeiro

        def __str__(self):
            return f"{self.titulo} ({'✓' if self.concluida else '✗'})"
