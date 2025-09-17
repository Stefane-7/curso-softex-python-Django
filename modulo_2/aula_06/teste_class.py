class Cachorro:
    def __init__(self, nome: str, cor: str) -> None:
        self.nome = nome
        self.cor  = cor

    def latir(self, fala: str) -> None:
        print(f"{self.nome} diz: {fala}!")


meu_cachoro = Cachorro("Rex", "preto")
fala = input("O que o cachorro vai dizer?: ")



# nome e cor são atributos (variaveis) da class Cachorro
# por isso não são chamadas com parênteses: ()
print(meu_cachoro.nome)
print(meu_cachoro.cor)

meu_cachoro.latir(f"{fala}!")