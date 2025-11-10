from django.contrib import admin
from .models import Tarefa, Execucao # 1. Importe seu Model
# Register your models here.
admin.site.register(Tarefa)
admin.site.register(Execucao)