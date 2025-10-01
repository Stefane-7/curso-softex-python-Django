"""Exercicio 1: Contando Ocorrências
Crie um programa que conte quantas vezes um numero especifico aparece em uma lista.
° ENTRADA: Uma lista de números e um número para ser procurado.
° SAIDA: Um número inteiro que representa a quantidade de vezes que o número procurado aparece na lista.

EXEMPLO: 
numero = [1,5,2,8,5,3,5]
numero_procurado = 5
resultado esperado:
3
"""

numero = [1,5,2,8,5,3,5]
numero_procurado = 6 

resultado = numero.count(numero_procurado)
print(resultado)