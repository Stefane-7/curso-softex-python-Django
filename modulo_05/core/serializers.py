from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        # Campos gerados automaticamente (não aceitos na entrada)
        read_only_fields = ['id', 'criada_em']
