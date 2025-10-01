from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self._materias = {}

    @property
    def notas(self):
        return self._materias 
    
    @notas.setter
    def notas(self, materia, nota):
        aula = self._materias.get(materia)
        if aula:
            aula.append(nota)
        else:
            self._materias[materia] = [nota]         
        