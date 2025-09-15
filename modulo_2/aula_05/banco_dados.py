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