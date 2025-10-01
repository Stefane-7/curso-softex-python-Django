"""1. Nível Fácil: Registro de Pessoas

Crie uma classe base Pessoa com um construtor que recebe nome e idade. Adicione um
método apresentar() que imprime uma frase com o nome e a idade da pessoa.

Em seguida, crie uma classe Estudante que herda de Pessoa. O construtor de Estudante deve
chamar o construtor da classe pai e adicionar um atributo para o curso. A classe Estudante
deve sobrescrever o método apresentar() para incluir o curso na frase.

Por fim, crie uma lista com um objeto Pessoa e um objeto Estudante. Itere sobre a lista e
chame o método apresentar() para cada item, demonstrando o polimorfismo."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá me chamo {self.nome} e tenho {self.idade} anos") 

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)           
        self.curso = curso

    def apresentar(self):
        print(f"Olá me chamo {self.nome} tenho {self.idade} e faço o curso: {self.curso}!")


pessoa_1 = Pessoa("Ana", 35)
pessoa_2 = Estudante("Paula", 28, "Contábeis")            

lista = [pessoa_1, pessoa_2]

for pessoa in lista:
    pessoa.apresentar()