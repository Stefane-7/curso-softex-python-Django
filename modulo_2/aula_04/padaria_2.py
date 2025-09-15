"""
comercio Padaria
1- O programa tem que rodar em loop infinito até ser parado
2- O cliente pedir um tipo de pão (frances, doce, pão de forma)
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
        "atendente": "Maria",
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

def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    """Caucula o valor do frete com base no bairro de entrega"""
    print("Bairros para entrega")
    for bairro in bairros_disponiveis.values():
        print(f"- {bairro['nome']}" )

    bairro_entrega_nome = input("Qual o bairro de entrega?").lower()
    bairro_encontrado = ""

    for chave, bairro in bairros_disponiveis.values():
        if bairro["nome"].lower() == bairro_entrega_nome:
            bairro_encontrado = chave
            break

    if not bairro_encontrado:
        print("Bairro fora da área de entrega. ")
        return None
    else: 
        frete = bairros_disponiveis[bairro_encontrado]["frete"]
        return bairro_entrega_nome, frete    

def cadastrar_produto(estoque: dict) -> None:
    """Permite ao funcionario cadastrar um novo produto"""
    nome_produto = input("Digite o nome do novo produto(identificador): ").lower()

    if nome_produto in estoque:
        print("Erro! Produto já cadastrado com esse identificador!!! ")
        return

    try:
        nome_completo = input("Digite o nome completo do produto: ")
        valor = float(input("Digite o valor do novo produto: "))
        quantidade = int(input("Digite a quantidade inicial do produto: "))

        if nome_produto and valor > 0 and quantidade > 0:
            estoque[nome_produto] = {"nome": nome_completo, "valor": valor, "quantidade": quantidade}
            print(f"Produto{nome_completo} cadastrado com sucesso!")

        else:
            print("Erro! Dados inválidos.")

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
                print(f" Quantidade atual de {estoque[nome_produto]['quantidade']} itens.")

            else:
                print("Quantidade inválida.")
        else:
            print("Erro! Opção inválida!")
    except ValueError:
        print("Erro! Entrada de dados inválida. Digite apenas números.")   

def cadastrar_localidade(bairros: dict) -> None:
    """Permite ao funcionario cadastrar um novo bairro para entrega"""
    nome_bairro = input("Digite o nome do bairro(identificador): ").lower().strip()
    if nome_bairro in bairros:
        print("Erro! Bairro já cadastrado.")
        return
    
    try:
        nome_completo = input("Digite o nome completo do bairro: ").strip()
        valor_frete = float(input(f"Digite o valor do frete para o bairro {nome_completo}: "))

        if nome_bairro and valor_frete >= 0 and nome_completo:
            bairros[nome_bairro] = {"nome": nome_completo, "frete": valor_frete}
            print(f"Localidade {nome_completo} com frete de R$ {valor_frete:.2f} foi cadastrado com sucesso!")
        else:
            print("Dados inválidos! O cadastro não foi realizado.")    

    except ValueError:
        print("Entrada inválida! Valor do deve ser um número. ") 


def processar_pedido(paes_disponiveis: dict) -> tuple[dict, int, float, dict] | None:
    """
       processa o pedido do client verifica o estoque e cálcula o frete.
       Retorna uma tupla com o dicionario do pão, quantidade, 
       valor total da compra e o dicionario atualizado de paes.   
    """

    print("Temos os seguintes pães: ")
    for pao in paes_disponiveis.values():
        print(f" - {pao["nome"]}")


    escolha_pao = input("Qual pão você deseja?: ").lower()
    pao_encontrado = ""

    for chave, pao in paes_disponiveis.items():
        if pao["nome"].lower() == escolha_pao:
            pao_encontrado = chave
            break
    
    if not pao_encontrado:
        print("Opção inválida!")
        return None

    pao_escolhido = paes_disponiveis[pao_encontrado]

    try:
        quantidade = int(input(f"Digite a quantidade do {pao_escolhido["nome"]}: "))
        
        if quantidade <= 0:
            print("Quantidade inválida")
            return None                 

    except ValueError:
        print("Erro! Quantidade deve ser um número inteiro")
        return None
    
    if quantidade > pao_escolhido["quantidade"]:
        print(f"Infelizmente só tenho {pao_escolhido['quantidade']} unidades deste pão.")
        return None
    
    paes_disponiveis[pao_encontrado]["quantidade"] -= quantidade
    valor_compra = quantidade * pao_escolhido["valor"]

    return pao_escolhido, quantidade, valor_compra, paes_disponiveis

                        



def iniciar_programa():
    """Fução que inicia o loop principal do programa de vendas"""

    banco_dados = dados() 

    atendente = banco_dados["atendente"]
    paes_estoque = banco_dados["paes"]
    bairros_disponiveis = banco_dados["bairros"]
    codigo_venda = banco_dados[ "codigo_vendas_base"]

    while True:
        print('-- Be vindo(a) a Padaia desespero, sou o(a) atendente {atendente}.')
        print('1. Iniciar vendas.')
        print('2. Gerenciar Produtos.')
        print('3. Cadastrar Nova Localidade.')
        print('4. Sair do Sistema.')

        opcao = input("Escolha a sua opção: ")

        if opcao == '1':
            pedido = processar_pedido(paes_estoque)

            if not pedido:
                continue

            pao_escolhido, qtd_pedido, valor_compra, paes_estoque = pedido
            print(f"Seu pedido foi de {qtd_pedido} - {pao_escolhido['nome']} total ficou em {valor_compra:.2f}.")

            forma_retirada = input("É para 1- retirar ou 2- entregar?: ")
            valor_frete = 0.0

            if forma_retirada == 2:
                bairro, valor_frete = calcular_frete(bairros_disponiveis)
                print(f"Valor do frete para o bairro {bairros_disponiveis[bairro]['nome']} é de R$ {valor_frete:.2f}")

            elif forma_retirada != '1':
                print('Opção inválida!')
                continue

            dados_cliente = obter_dados_clientes()
            forma_pagamento = solicitar_forma_pagamento()

            valor_total_compra = valor_frete + valor_compra
            cod_venda = gerar_codigo_venda(cod_venda) 
            banco_dados["codigo_vendas_base"] = cod_venda

            print('--Resumo de venda--')
            print(f'Cliente: {dados_cliente["nome"]}')
            print(f'Valor dos pães: R$ {valor_compra:.2f}')
            print(f'Valor frete: R$ {valor_frete:.2f}')
            print(f"Forma de pagamento: {forma_pagamento}")
            print(f"Valor total da compra R$ {valor_total_compra}")
            print(f"Código da entrega: {cod_venda}")

        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            print("Saindo do sistema. Até a próxima!")
            break
        else:
            print("Opção inválida.")
