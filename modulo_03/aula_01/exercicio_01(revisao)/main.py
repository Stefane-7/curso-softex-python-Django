"""Etapa 4: Juntando Tudo (no arquivo main.py)
Este é o arquivo principal, onde você vai "ligar o motor" e ver tudo funcionando.
Seu trabalho aqui:

● Importe as classes Escola e Estudante que você criou.

● Crie uma instância (um objeto) da sua Escola.

● Crie pelo menos dois objetos da sua classe Estudante, dando a cada um um nome, idade e matrícula.

● Use os métodos que você criou para:

○ Adicionar algumas matérias e notas para cada estudante.

○ Adicionar os estudantes à sua Escola.

● Chame o método mostrar_relatorio() da sua Escola para ver a mágica acontecer!"""



from estudante import Estudante
from escola import Escola


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