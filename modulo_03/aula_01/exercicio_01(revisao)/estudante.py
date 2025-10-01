from pessoa import Pessoa

class Estudante(Pessoa):
    materias = {}
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        #self.materias = {}

    def add_nota_materia(self, materia, nota):
        aula = materias.get(materia)
        if aula:
            aula.append(nota)
        else:
            materias[materia] = [nota]         
        