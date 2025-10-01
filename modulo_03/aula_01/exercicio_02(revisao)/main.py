"""Etapa 4: Juntando Tudo (no arquivo main.py)
Este é o arquivo principal, onde você vai "ligar o motor" e ver tudo funcionando.
Seu trabalho aqui:
● Importe as classes Escola e Estudante que você criou.
● Crie uma instância (um objeto) da sua Escola.
● Crie pelo menos dois objetos da sua classe Estudante, dando a cada um um nome, idade e matrícula.
● Use os métodos que você criou para:
○ Adicionar algumas matérias e notas para cada estudante.
○ Adicionar os estudantes à sua Escola.
● Chame o método mostrar_relatorio() da sua Escola para ver a mágica acontecer!"""

"""from estudante import Estudante
from escola import Escola
from""" 

class Loja:
    def __init__(self):
        self.produtos = []
        self.estoque = {}

    def adicionar_produto_ao_estoque(self, produto, quantidade):
        self.produtos.append(produto)
        self.estoque[produto.nome] = quantidade
        produto.set_quantidade_em_estoque(quantidade)

    def verificar_estoque_de_produto(self, nome_produto):
        return self.estoque.get(nome_produto, 0)