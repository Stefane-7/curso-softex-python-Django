class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade

    
    def get_nome(self):
        return self._nome  
        
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
            
 
class Escola:
    def __init__(self,):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        if isinstance(estudante, Estudante):
            self.estudantes.append(estudante)
        else:
            print("Erro: apenas objetos do tipo Estudante podem ser adicionados.")


    def mostrar_relatorio(self):
        print("Relatório da Escola")
        print("=" * 40)
        
        if not self.estudantes:
            print("Nenhum estudante cadastrado.")
        
        else:
            for estudante in self.estudantes:
                estudante.apresentar()
                for materia, notas in estudante.materias.items():
                    print(f'{materia}: {notas}\n\n')           
                    
estudante1 = Estudante('Maria', 21, 32495089)
estudante2 = Estudante('Roberta', 45, 25901012)

estudante1.set_nota('Matemática', 10.0)
estudante1.set_nota('Matemática', 5.6)
estudante2.set_nota('Português', 9.00)
estudante2.set_nota('Português', 8.0)

escola1 = Escola()

escola1.adicionar_estudante(estudante1)
escola1.adicionar_estudante(estudante2)

escola1.mostrar_relatorio()                    