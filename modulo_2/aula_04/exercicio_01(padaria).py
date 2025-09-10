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


def dados() -> dict:
    """Carregar e retornar os dados de produtos, frete e funcionários"""
    return{
        "atendnte": "Maria",
        "paes": {
            "frances": { "nome": "Pão Frances", "valor": 0.50, "quantidade": 15},
            "doce": {"nome": "Pão Doce", "valor": 5.00, "quantidade": 20},
            "forma": {"nome": "Pão de Forma", "valor": 5.99, "quantidade": 18}

        },
        "bairros": {
            "barroco": {"nome": "Barroco", "frete": 5.00},
            "sao jose": {"nome": "São José", "frete": 15.00}
        },
        "codigo_vendas_base": 95875, 

    }
def obter_dados_clientes() -> dict:
    """solicitar e retornar os dados dos clientes"""
    nome = input("Informe seu nome: ")
    return {"nome": nome}

def solicitar_forma_pagamento() -> str:
    """solicitar e retornar a forma de pagamento escolhida"""
    while True:
        pagamento = input("Escolha a forma de pagamento (1- Dinheiro, 2-Cartão)")
        if pagamento == "1":
            return "Dinheiro"
        elif pagamento == "2":
            return "Cartão"
        else:
            print("Forma de pagamento inválida.")

def gerar_codigo_venda(codigo_base: int) -> int:
    """gera e retorna o codigo de venda"""
    return codigo_base + 1

def caucular_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    """Caucula o valor do frete com base no bairro de entrega"""
    print("Bairros para entrega")
    for bairro in bairros_disponiveis.values():
        print(f"- {bairro[nome]}" )

    bairro_entrega_nome = input("Qual o bairro de entrega?").lower()
    bairro_encontrado = ""

    for chave, bairro in bairros_disponiveis.values():
        if bairro[nome].lower() == bairro_entrega_nome:
            bairro_encontrado = chave
            break

    if not bairro_encontrado:
        print("Bairro fora da área de entrega. ")

    else: 
        frete = bairros_disponiveis[bairro_encontrado]["frete"]
        return bairro_entrega_nome, frete    

def cadastrar_produto(estoque: dict) -> None:
    """Permite ao funcionario cadastrar um novo produto"""
    nome_produto = input("Digite o nome do novo produto(identificador): ").lower()

    if nome_produto in estoque:
        print("Erro! Produto á cadastrado cpm esse identificador!!! ")

    try:
        nome_completo = ("Digite o nome completo do produto: ")
        valor = float(input("Digite o valor do novo produto: "))
        quantidade = int(input("Digite a quantidade inicial do produto: "))

        if nome_produto and valor > 0 and quantidade > 0:
            estoque[nome_produto]: {"nome": nome_completo, "valor": valor, "quantidade": quantidade}
            print(f"Produto{nome_completo} cadastrado com sucesso!")

        else:
            print("Erro! Dados invalidos.")

    except ValueError:
        print("Entrada de dados inválida.")   

def atualizar_produto(estoque: dict) -> None:
    """Permite o funcionário atualizar um produto existente"""
    nome_produto = input("Digite o nome do produto para atualizar (identificador): ").lower()
    

    if nome_produto not in estoque:
        print("Produto não cadastrado.")
        return
    print(f"Produto '{estoque[nome_produto]}' selecionado")
    escolha = input("O que deseja atualizar?\n \
                    1 - valor;\n \
                    2 - quantidade")
    
    try:
        if escolha == "1":
            novo_valor = float(input("Digite o novo valor do produto: "))
            if novo_valor > 0:
                estoque[nome_produto]["valor"] = novo_valor
                print(f"Valor atualizado para R$ {novo_valor:.2f} ")
            else:
                print("Valor inválido!") 

        elif escolha == "2":
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            if nova_quantidade > 0:
                estoque[nome_produto]["quantidade"] = nova_quantidade
                print(f" Quantidade atual de {estoque[nome_produto]["quantidade"]} itens.")

            else:
                print("Quantidade inválida.")
        else:
            print("Erro! Opção inválida!")
    except ValueError:
        print("Erro! Entrada de dados inválida. Digite apenas números.")                          