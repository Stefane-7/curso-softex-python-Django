"""Crie um programa que funcione como uma calculadora de bolso. Ele deve ser capaz de fazer
adição, subtração, multiplicação e divisão.
O programa deve sempre mostrar um menu de opções, pedir ao usuário para escolher a
operação e digitar dois números. No final, ele exibe o resultado da conta. Se houver algum
erro, como uma divisão por zero ou o usuário digitar algo que não é um número, o programa
deve avisar e não travar."""


def calculadora():
    while True:
        print("\n--- CALCULADORA DE BOLSO ---")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Saindo da calculadora. Até logo!")
            break

        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: você deve digitar apenas números!")
            continue

        try:
            if opcao == "1":
                resultado = n1 + n2
                print(f"Resultado: {n1} + {n2} = {resultado}")
            elif opcao == "2":
                resultado = n1 - n2
                print(f"Resultado: {n1} - {n2} = {resultado}")
            elif opcao == "3":
                resultado = n1 * n2
                print(f"Resultado: {n1} * {n2} = {resultado}")
            elif opcao == "4":
                resultado = n1 / n2
                print(f"Resultado: {n1} / {n2} = {resultado}")
            else:
                print("Opção inválida! Escolha entre 1 e 5.")
        except ZeroDivisionError:
            print("Erro: não é possível dividir por zero!")

calculadora()

