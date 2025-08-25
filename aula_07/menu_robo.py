"""crie um programa que simula o controle de um robo simples com um menu de comando.
1 -  robo pode estar em posição inicial (pode usar uma posição 0)
2 - O programa deve exibir um menu com as segintes opções: 1 - Avançar, 2 - Recuar, 3 - status, 4 - Desligar.
3 - Peça ao usuariopara escolher um comando
4 - Com base no comando execute a ação correspondente:
    avançar: adiocione uma valor a posição do robo
    recuar: subtrair um valor da psição do robo
    status: ostre a posição do robo
    desligar: encerreo programa
5 - o menu deve continuar aparecendo após cada comando até o usuario desligar
6 - se o suario digitar um comando invalido exiba uma mensagem de erro"""

robo = 0

while True:
    escolha = int(input('Escolha um comando: 1-Avançar: 2-Recuar: 3-Status: 4-Desligar:'))
    if escolha == 1:
        robo += 1
    elif escolha == 2:
        robo -= 1
    elif escolha == 3: 
        print(f'O robo esta na posiição: {robo}')
    elif escolha == 4:
        print('Desligando sistema.')
        break
    else:
        print('Erro: Digite um comando valido.')    
