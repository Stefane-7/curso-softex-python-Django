from rest_framework import serializers
from .models import Tarefa
from datetime import date

class TarefaSerializer(serializers.ModelSerializer):

    # campo personalizado precisa ser declarado fora da Meta
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
        }
    )

    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida','criada_em','prioridade','prazo', 'data_conclusao']
        read_only_fields = ['id', 'criada_em']


    def validate_titulo(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )

        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )
        
        return value


    def validate(self, data):
        prazo = data.get('prazo')
        concluida = data.get('concluida', False)
        request = self.context.get('request')

        if prazo and prazo < date.today():
            raise serializers.ValidationError(
                {'prazo': 'O prazo não pode ser uma data no passado.'}
)

        
        if not concluida and prazo is None:
            raise serializers.ValidationError(
                {'prazo': 'O prazo é obrigatório quando a tarefa não está concluída.'}
                
)
            
        metodo = request.method if request else None

        prioridade = data.get(
            'prioridade',
            getattr(self.instance, 'prioridade', None)
        )

        if (
            prioridade == 'alta'
            and concluida is True
            and metodo == 'PATCH'
        ):
            raise serializers.ValidationError({
                'concluida': 'Tarefas com prioridade ALTA só podem ser concluídas via PUT.'
            })    
        
        prioridade_atual = self.instance.prioridade

        if (
            prioridade_atual == 'alta'
            and 'prioridade' in data
            and metodo == 'PATCH'
        ):
            raise serializers.ValidationError({
                'prioridade': 'A prioridade de uma tarefa ALTA não pode ser alterada via PATCH.'
            })    

        concluida_atual = (
        concluida 
        
        if concluida is not None 
        else getattr(self.instance, 'concluida', False)
    )

        if concluida_atual:
            
            data['data_conclusao'] = date.today()
        else:
            
            data['data_conclusao'] = None
        
        return data
