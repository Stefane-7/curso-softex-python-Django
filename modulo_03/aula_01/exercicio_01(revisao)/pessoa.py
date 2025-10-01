"""Etapa 1: A Pessoa (no arquivo pessoa.py)
Toda escola tem pessoas. Um estudante é uma pessoa, um professor é uma pessoa. Vamos criar um "molde" básico para qualquer pessoa.
Seu trabalho aqui:

● Crie uma classe (o nosso molde) chamada Pessoa.

● Essa classe deve ter um nome e uma idade.

● Para garantir que as informações sejam acessadas e modificadas de forma organizada, implemente um método "getter" para o nome. Um "getter" é uma forma de obter a informação de um objeto."""

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade

    
    def get_nome(self):
        return self._nome    