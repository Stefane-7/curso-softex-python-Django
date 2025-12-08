from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        # Campos gerados automaticamente (não aceitos na entrada)
        read_only_fields = ['id', 'criada_em']

    def validate_titulo(self, value):
   
        value = value.strip()

        # Validação 1: Não vazio
        if not value:
            raise serializers.ValidationError(
            "O título não pode ser vazio ou conter apenas espaços."
            )

        # Validação 2: Mínimo de caracteres
        if len(value) < 3:
            raise serializers.ValidationError(
            "O título deve ter pelo menos 3 caracteres."
            )

        # Validação 3: Não apenas números
        if value.isdigit():
            raise serializers.ValidationError(
            "O título não pode conter apenas números."
            )

        return value

