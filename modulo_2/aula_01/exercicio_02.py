'''Nível 2: Combinando Lógica
Aqui, você vai usar mais de uma lista e combinar diferentes lógicas de controle, como loops e
verificações de pertencimento.

     Exercício 2: Encontrando Elementos Comuns
Você tem duas listas e precisa encontrar os elementos que aparecem em ambas. O programa
deve gerar uma terceira lista contendo apenas os elementos em comum, sem repetições.
● Entrada: Duas listas.
● Saída: Uma nova lista com os elementos que as duas listas têm em comum.
Exemplo:
lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
Resultado Esperado:
['azul', 'verde']'''


lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]

em_comum = []

for item in lista1:
    if item in lista2:
        em_comum.append(item)
print(lista2)
print(lista1)
print(f'Os itens em comum entre as listas são: {em_comum}')

