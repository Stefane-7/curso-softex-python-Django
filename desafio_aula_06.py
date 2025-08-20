"""
comercio Padaria
1- O programa tem que rodar em loop infinito até ser parado
2- O cliente pedir um tipo de pão (frances, doce, pão de forma, australiano)
3- cada pão vai ter uma quantidade
4- valor do pão
5- pedir forma de pagamento (dinheiro, cartao)
6- forma de entrega
7- dados do cliente (se for entrega)
8- valor do frete de frete por bairro
9- nome da atendente
10- codigo da entrega
"""

nome_frances = "frances"
nome_doce = "doce"
nome_forma = "forma"
valor_fances = 0.50
valor_doce = 5.00
valor_forma = 5.99

quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

nome_atendente = "maria"

bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

frete_barroco = 5.00
frete_sao_jose = 15.00

codigo_de_vendas = 98568

contador = 0

while True:
   print(F'--Bem vindo a padaria Desespero, sou a atendente {nome_atendente}')
   escolha = input(f'Temos os pães: {nome_frances, nome_doce, nome_forma}')
   if escolha == nome_frances:
      quantidade = int(input('Qual a quantidade: '))
     if quantidade <= quantidade_frances:
         quantidade_frances -= quantidade
         pedidio_de_paes = quantidade
         valor_compra = quantidade * valor_fances
         print(f'Seu pedidio ficou em R$ {valor_compra}.')
    else:
      print(f'infelizmente só tenho {quantidade_frances} pães no momento.')

    forma_retirada = input('É para 1: retirar ou 2: entregar?').lower()
    if forma_retirada == "2":
    bairro_entrega = input(f'Qual o bairro?  ( 1:{bairro_barroco} 2:{bairro_sao_jose})')
    if bairro_entrega ==  '1'
        valor_frete = frete_barroco
        print(f'Valor do frete ficou R$ {valor_frete}')
    elif bairro_entrega == '2':
        valor_frete = frete_sao_jose
        print(f'Valor do frete ficou R$ {valor_frete}')
    else:
        print('fora da area de entrega')
        break
    elif forma_retirada == '1'
    valor_frete = 00.00
    else: 
        break

    dados_cliente = input("Informe seu nome")
    forma_pagamento = input('Escolha a forma de pagamento (1-dinheiro, 2-cartão)')

    if forma_pagamento == "1":
    forma_pagamento = "Dinheiro"
    else:
        forma_pagamento = "Cartão"

    codigo_atual = codigo_atual + 1  

    print(f'O valor total da sua compra foi de R$ {valor_compra + valor_frete} com codigo de entrega {codigo_atual}.')
