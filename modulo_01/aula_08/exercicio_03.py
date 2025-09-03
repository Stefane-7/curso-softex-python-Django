"""crie um programa que codifica  e decodifica uma frase, seguindo as regras abaixo.
cada vogal deve ser substituida pelo numero correspondente:
a = 1
e = 2
i = 3
o = 4
u = 5

o programa deve:
1 - ler uma frase digitada pelo usuario.
2 - exibir a frase codificada, trocando as vogais pelos numeros.
3 - exibir a frase decodificada, voltando os numeros as vogais originais."""

frase = input('Digite uma frase: ').lower()
nova = frase.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")

print(nova)
print(frase)