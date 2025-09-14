"""Crie um programa que recebe uma frase do usuário e faz uma análise completa sobre ela,
mostrando:
● A quantidade de palavras na frase.
● A quantidade de vogais (a, e, i, o, u).
● A quantidade de consoantes.
● Se a frase é um palíndromo (ou seja, se ela pode ser lida da mesma forma de trás para
frente, ignorando espaços e letras maiúsculas)."""


def contador_vogais_consoantes(frase: str) -> None:
    vogais = "aeiou"
    contador_vogais = 0
    contador_consoantes = 0

    for letra in frase.replace(" ", ""):
        if letra in vogais:
            contador_vogais += 1
        elif letra not in vogais and letra.isalpha():
            contador_consoantes += 1

    print(f"Vogais: {contador_vogais}")
    print(f"Consoantes: {contador_consoantes}")


def contador_palavras(frase: str) -> int:
    palavras = len(frase.split())
    print(f"Palavras: {palavras}")


def verificador_palindromo(frase: str) -> None:
    frase_formatada = frase.lower().replace(" ", "")
    if frase_formatada == frase_formatada[::-1]:
        print("É um palíndromo? Sim")
    else:
        print("É um palíndromo? Não")


frase = input("Digite uma frase: ")
print("--- Resumo da Análise ---")
contador_palavras(frase)
contador_vogais_consoantes(frase)
verificador_palindromo(frase)
