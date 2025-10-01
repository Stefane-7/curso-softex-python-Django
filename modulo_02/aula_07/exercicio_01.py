"""Exercício 1: Classe Pessoa
Objetivo: Criar uma classe com validações simples nos setters para tipo e valor.

● Requisitos:

1. Crie uma classe Pessoa com os atributos protegidos _nome e _idade.

2. Crie uma @property para nome.

3. Crie um @nome.setter que valide se o valor é uma string e não está vazio.

4. Crie uma @property para idade.

5. Crie um @idade.setter que valide se a idade é um número inteiro e positivo.

6. No __init__, use os setters para atribuir os valores iniciais (ex: self.nome = nome).

7. Instancie um objeto Pessoa com dados válidos e depois tente alterar nome para um

valor vazio e idade para um valor negativo para testar as validações."""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
        

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str) and novo_nome:
            self._nome = novo_nome

        else:
            print("Erro! O novo nome não deve ser uma string vazia.")  

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade: int):
        if isinstance(nova_idade, int) and nova_idade >0:
            self._idade = nova_idade

        else:
            print("Erro! Nova idade precisa ser um número positivo.")    


nova_pessoa = Pessoa("Anderson", 42)


print(nova_pessoa.nome)
print(nova_pessoa.idade)

            

