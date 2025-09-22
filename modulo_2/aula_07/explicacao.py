
# explicação 01
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.__preco = preco
        

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, valor):
        if self._verifica_valor(valor):
            self.__preco = valor

        else:
            print("Valor incorreto!") 


    def _verifica_valor(self, valor):
        return valor >= 0

   
# explicação 03   
caneta = Produto("Caneta  Azul", 2.50) 
caneta.set_preco(10)
print(caneta.get_preco())  


class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if self._verifica_valor(valor):
            self.__preco = valor
        else:
            print("Valor incorreto!")

    def _verifica_valor(self, valor):
        return valor >= 0
    
caneta = Produto("Caneta Azul", 10)
print(caneta.preco)
caneta.preco = -10