"""Etapa 1: O Produto Genérico (no arquivo produto.py)
Toda loja vende produtos. O produto é a "peça" principal do nosso sistema. Vamos criar um molde genérico que todo produto terá.
Seu trabalho aqui:
● Crie uma classe (o nosso molde) chamada Produto.
● Essa classe deve ter um nome, um preco e uma quantidade_em_estoque.
● Para garantir que as informações sejam acessadas e modificadas de forma organizada, implemente um método "getter" para o preço. Isso nos ajuda a manter o código limpo.
● Adicione um método "setter" para atualizar a quantidade em estoque."""

class Produto:
  def __init__(self, nome, preco, quantidade_em_estoque):
    self.nome = nome
    self._preco = preco
    self.quantidade_em_estoque = quantidade_em_estoque
    
    def get_preco():
      return self._preco
      
    def atualizar_quantidade(self):
      pass