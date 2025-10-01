class Produto:
  def __init__(self, nome, preco, quantidade_em_estoque):
    self.nome = nome
    self._preco = preco
    self.quantidade_em_estoque = quantidade_em_estoque
    
    def get_preco():
      return self._preco
      
    def atualizar_quantidade(self):
      pass
    
    
    
class ProdutoEletronico(Produto):
  def __init__(self, nome, preco, quantidade_em_estoque, tempo_garantia_meses):
    super().__init__(nome, preco, quantidade_em_estoque)
    self.tempo_garantia_meses = tempo_garantia_meses
    
    
class Loja:
  def __init__(self, estoque):
    self.estoque = []
  
