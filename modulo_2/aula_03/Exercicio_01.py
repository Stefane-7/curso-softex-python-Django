agenda = {}

while True:
    print("\n--- MENU ---")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso!")
        
    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "3":
        print("Saindo da agenda...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")