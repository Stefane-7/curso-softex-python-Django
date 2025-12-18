from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
from datetime import date
import logging
from rest_framework.permissions import IsAuthenticated
from .permissions import PodeDeletarTarefa, PodeEditarTarefa
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)

class ListaTarefasAPIView(ListCreateAPIView):
    

    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ownership: usuário só vê as próprias tarefas
        return Tarefa.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
       
        serializer.save(user=self.request.user)


class TarefasEstatisticasAPIView(APIView):
    

    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = Tarefa.objects.filter(concluida=False).count()

        taxa_conclusao = concluidas / total if total > 0 else 0

        dados = {
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": round(taxa_conclusao, 2)
        }

        return Response(dados, status=status.HTTP_200_OK)
    
class DetalheTarefaAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = TarefaSerializer

    def get_queryset(self):
        
        return Tarefa.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), PodeDeletarTarefa()]

        if self.request.method == 'PUT':
            return [IsAuthenticated(), PodeEditarTarefa()]

        return [IsAuthenticated()]
    
class DuplicarTarefaAPIView(APIView):
    def post(self, request, pk):
        tarefa_original = get_object_or_404(Tarefa, pk=pk)

        nova_tarefa = Tarefa.objects.create(
            titulo=tarefa_original.titulo + " (cópia)",
            concluida=False,
            data_conclusao=None
        )

        serializer = TarefaSerializer(nova_tarefa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConcluirTodasTarefasAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        hoje = date.today()

        Tarefa.objects.update(concluida=True, data_conclusao=hoje)

        return Response(
            {"mensagem": "Todas as tarefas foram concluídas."},
            status=status.HTTP_200_OK
        )

class MinhaView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user

        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_staff": user.is_staff,
                "date_joined": user.date_joined
            },
            status=status.HTTP_200_OK
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception:
            return Response(
            {"detail": "Token inválido."},
            status=status.HTTP_400_BAD_REQUEST
        ) 
            
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            return Response(
                {"error": "Informe a senha atual e a nova senha."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not user.check_password(old_password):
            return Response(
                {"error": "Senha atual incorreta."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"detail": "Senha alterada com sucesso."},
            status=status.HTTP_200_OK
        )       
        