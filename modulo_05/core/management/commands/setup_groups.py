from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Tarefa

class Command(BaseCommand):
    help = "Cria grupos e permissões do sistema (RBAC)"

    def handle(self, *args, **options):

        
        tarefa_ct = ContentType.objects.get_for_model(Tarefa)

       
        permissoes = {
            "pode_criar_tarefa": "Pode criar tarefa",
            "pode_editar_tarefa": "Pode editar tarefa",
            "pode_deletar_tarefa": "Pode deletar tarefa",
            "pode_ver_estatisticas": "Pode ver estatísticas",
        }

        permissoes_obj = {}

        for codename, nome in permissoes.items():
            perm, _ = Permission.objects.get_or_create(
                codename=codename,
                name=nome,
                content_type=tarefa_ct
            )
            permissoes_obj[codename] = perm

        
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        user_group, _ = Group.objects.get_or_create(name="Usuario")

        

        # Admin -> tudo
        admin_group.permissions.set(permissoes_obj.values())

        # Editor -> criar e editar
        editor_group.permissions.set([
            permissoes_obj["pode_criar_tarefa"],
            permissoes_obj["pode_editar_tarefa"],
        ])

        # Usuario → nenhuma permissão extra
        user_group.permissions.clear()

        self.stdout.write(self.style.SUCCESS("Grupos e permissões configurados com sucesso."))
