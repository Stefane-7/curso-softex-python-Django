def calcula_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
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