from rest_framework.permissions import BasePermission

class PodeDeletarTarefa(BasePermission):
    """
    Permite deletar tarefa apenas para usuários
    com a permissão 'pode_deletar_tarefa'
    """

    def has_permission(self, request, view):
        return request.user.has_perm("core.pode_deletar_tarefa")



class PodeEditarTarefa(BasePermission):
    """
    Permite edição completa (PUT) apenas
    para usuários com permissão específica.
    """

    def has_permission(self, request, view):
        return request.user.has_perm("core.pode_editar_tarefa")
    