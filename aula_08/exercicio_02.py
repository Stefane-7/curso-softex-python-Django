"""Cire um programa que recebe um numero de telefone com 11 digitos

1 - o numero é considerado invalido se tiver 3 numeros iguais.

2 - O programa deve verificar se o numero tem 11digitos e se todos os caracteres são numeros.

3 - se o numero for valido, o programa deve formata-lo para o padrão (xx) xxxx-xxxx.

4 - O programa deve imprimir o numero formatado ou a mensagem de erro correspondente"""

numero = input("Digite seu número de telefone: ")

if len(numero) != 11:
    print("Número com tamanho incorreto.")
elif not numero.isdigit():
    print("Não é possivel gerar um numero de telefone com esses valores")    
else:
    valido = True
    for c in numero:
        cont = 0
        for d in numero:
            if d == c:
                cont += 1
        if cont >= 3:
            valido = False
            break
    if not valido:
        print("Digite um telefone valido!")
    else:
        print("("+numero[0]
        +numero[1]+")" 
        +numero[2]
        +numero[3]
        +numero[4]
        +numero[5]
        +numero[6] 
        + "-" 
        +numero[7]
        +numero[8]
        +numero[9]
        +numero[10])                   
