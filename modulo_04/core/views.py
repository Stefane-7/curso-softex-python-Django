from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def home_2(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1>Olá, Mundo! Esta é minha segunda página Django!</h1>")