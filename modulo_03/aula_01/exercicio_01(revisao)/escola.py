"""Etapa 3: A Escola (no arquivo escola.py)
Uma escola é um lugar que contém muitos estudantes. Ela não é um estudante, mas tem uma coleção deles. Isso é o conceito de Composição.
Seu trabalho aqui:

●Crie uma classe chamada Escola.

● Esta classe deve ter uma lista para guardar todos os objetos Estudante.

● Crie um método adicionar_estudante() para colocar novos estudantes na lista da escola.

● Crie um método mostrar_relatorio() que percorre a lista de estudantes e imprime todas as suas informações: nome, matrícula, e as notas de cada matéria."""


from estudante import Estudante

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
                
                