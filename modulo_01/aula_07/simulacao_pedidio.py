"""Crie um programa que simule um pedidio em uma lanchonete
1 - Defina o preço de um hamburguer.
2 - Defina um codigo de cupom de desconto.
3 - O programa deve pedir ao cliente o nome do produto repetidamente até que o produto correto seja digitado.
4 - Após a escolha, o prorama deve perguntar se o cliente tem um cupom de desconto.
6 - Calcule o preço final e exiba o total a pagar.
7 - o programa deve encerrar após o pedidio ser finalizado"""


hamburguer_preco = 15.00

cupom_desconto = "desconto10"


while True:
    pedido = input('escolha seu pedidio: ')
    if pedido == 'hamburguer':
        print("pedido aceito.")
        break
    else:
        print('esse lanche não esta cadastrado, tente novamente. ') 

cupom = input('Digite um cupom de desconto: ')
if cupom == cupom_desconto:
    print(f'Seu lanche custou {hamburguer_preco *0.9}')
else:
    print(f'Seu lanche custou {hamburguer_preco}')       