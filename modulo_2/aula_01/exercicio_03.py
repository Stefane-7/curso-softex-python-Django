"""Nível 3: Lógica Avançada
Neste nível, os desafios exigem mais de uma lista e combinam diferentes lógicas de controle,
como loops e verificações de pertencimento.
   
   Exercício 3: Filtrando Números Primos
Sua tarefa é criar um programa que percorra uma lista de números e crie uma nova lista
contendo apenas os números que forem primos.
 
 ● Entrada: Uma lista de números inteiros.
 
 ● Saída: Uma nova lista com os números primos encontrados.

Exemplo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Resultado Esperado:
[2, 3, 5, 7]
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_primos = []

for numero in numeros:
    eh_primo = 2
    if numero < 2:
        eh_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False
                break
    if eh_primo:
        numeros_primos.append(numero)                
print(f'lista original: {numeros}')
print(f'lista de númers primos: {numeros_primos}')        