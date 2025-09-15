from banco_dados import dados
from dados_cliente import obter_dados_clientes
from caucular_frete import calcula_frete
from dados_pagamento import solicitar_forma_pagamento
from gerar_codigo import gerar_codigo_venda
from  gerenciar_localidade import cadastrar_localidade
from gerenciar_produto import cadastrar_produto, atualizar_produto
from gerenciar_pedido import processar_pedido


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

            forma_retirada = input("É para 1 - retirar ou 2 - entregar?: ")
            valor_frete = 0.0

            if forma_retirada == '2':
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
