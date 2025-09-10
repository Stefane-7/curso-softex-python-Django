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
