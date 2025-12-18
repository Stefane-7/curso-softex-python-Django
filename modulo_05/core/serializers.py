from django.contrib.auth.models import User, Group
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
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'user', 'concluida','criada_em','prioridade','prazo', 'data_conclusao']
        read_only_fields = ['id', 'user', 'criada_em']


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
        request = self.context.get('request')
        metodo = request.method if request else None
        prazo = data.get('prazo')
        concluida = data.get('concluida', getattr(self.instance, 'concluida', False))
        

        if prazo and prazo < date.today():
            raise serializers.ValidationError(
                {'prazo': 'O prazo não pode ser uma data no passado.'}
)

        
        if not concluida and prazo is None:
            raise serializers.ValidationError(
                {'prazo': 'O prazo é obrigatório quando a tarefa não está concluída.'}
                
)
            

        if self.instance:

            prioridade_atual = self.instance.prioridade
            prioridade_nova = data.get('prioridade', prioridade_atual)

          
            if (
                prioridade_atual == 'alta'
                and concluida is True
                and metodo == 'PATCH'
            ):
                raise serializers.ValidationError({
                    'concluida': 'Tarefas com prioridade ALTA só podem ser concluídas via PUT.'
                })

           
            if (
                prioridade_atual == 'alta'
                and prioridade_nova != prioridade_atual
                and metodo == 'PATCH'
            ):
                raise serializers.ValidationError({
                    'prioridade': 'A prioridade de uma tarefa ALTA não pode ser alterada via PATCH.'
                })

        
        if concluida:
            data['data_conclusao'] = date.today()
        else:
            data['data_conclusao'] = None

        return data
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    
    # Definimos 'write_only=True' para que a senha seja aceita no cadastro (POST),
    # mas NUNCA seja devolvida na resposta (Response JSON).
    password = serializers.CharField(
    write_only=True,
    required=True,
    style={'input_type': 'password'}
    )
    
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "As senhas não conferem."}
            )
        return data
    
    def create(self, validated_data):
        """
        Intercepta a criação para usar o 'create_user' e hashear a senha.
        """
        validated_data.pop('password2')

        # Extrai a senha dos dados validados
        password = validated_data.pop('password')
        # Extrai email e username
        email = validated_data.get('email', '')
        username = validated_data['username']
        # Cria a instância usando o método seguro do Django
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password 
        )
        
        try:
            grupo_usuario = Group.objects.get(name='Usuario')
            user.groups.add(grupo_usuario)
        except Group.DoesNotExist:
            pass 
        
        return user       