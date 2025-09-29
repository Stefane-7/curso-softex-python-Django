"""5. Casa e Cômodos (Médio)

● Classes: Comodo e Casa.

● Classe Comodo:

○ Atributo: nome.

○ Método: __init__(nome).

● Classe Casa:

○ Atributo (Composição): comodos, que deve ser uma lista vazia.

○ Método: __init__ que inicializa a lista comodos.

○ Método: adicionar_comodo(nome) que cria uma instância de Comodo e a adiciona
na lista comodos.

○ Método: listar_comodos() que itera sobre a lista e imprime o nome de cada cômodo"""


class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self, comodos: list[Comodo]):
        self.comodos = comodos
    
    def adicionar(self, comodo: Comodo):
        self.comodos.append(comodo) 

    def listar_comodos(self):
        for comodo in self.comodos:
            print(comodo.nome)

comodo1 = Comodo('sala')
comodo2 = Comodo('Cozinha')
lista_comodos = [comodo1, comodo2]

casa = Casa(lista_comodos)

casa.listar_comodos()
