"""Etapa 2: O Estudante Especializado (no arquivo estudante.py) Um estudante é uma pessoa, mas tem algumas características extras. Ele tem uma matrícula e tira notas.

Seu trabalho aqui:

● Crie uma classe chamada Estudante que herda (pega emprestado) todas as características da classe Pessoa.

● Adicione um atributo de matrícula a esta classe.

● Para guardar as notas, use um dicionário, onde a "chave" é o nome da matéria (como 'Matemática') e o "valor" é uma lista de notas (ex: [9.0, 8.5]).

● Crie um método "setter" para adicionar notas a uma matéria específica. Um "setter" é uma forma de definir ou alterar uma informação dentro do objeto."""


from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.materias = {}

    def apresentar(self):
        print(f'Nome: {self.get_nome()}\nIdade: {self.idade}\nMatricula: {self.matricula}')
    
    def set_nota(self, materia, nota):
        aula = self.materias.get(materia)
        if aula:
            aula.append(nota)
        else:
            self.materias[materia] = [nota]         
        

