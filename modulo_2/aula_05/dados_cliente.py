def obter_dados_clientes() -> dict:
    """solicitar e retornar os dados dos clientes"""
    nome = input("Informe seu nome: ")
    return {"nome": nome}