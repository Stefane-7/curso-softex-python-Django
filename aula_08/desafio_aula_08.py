"""Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número."""

print("###Validador de Triangulos###")

while True:
  lA = input("Digite o 1° valor: ")
  lB = input("Digite o 2° valor: ")
  lC = input("Digite o 3° valor: ")
  if lA.isdigit() and lB.isdigit() and lC.isdigit():
     lA = int(lA)
     lB = int(lB)
     lC = int(lC)
     if lA > 0 and lB > 0 and lC > 0:
        break
  else:
     print("Digite apenas numeros maiores que '0'!")
condicao_soma = (lA < lB + lC) and (lB < lA + lC) and (lC < lA + lB)
condicao_diferenca = (lA > abs(lB - lC)) and (lB > abs(lA - lC)) and (lC > abs(lA - lB))
if condicao_soma and condicao_diferenca:
  print(f"Os valores {lA}, {lB} e {lC} formam um triângulo")
else:
  print(f"Os valores {lA}, {lB} e {lC} não formam um triângulo")
     