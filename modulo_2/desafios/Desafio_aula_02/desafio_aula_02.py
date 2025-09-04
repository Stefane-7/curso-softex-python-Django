dados_de_acesso = []
while True:
    try:
      nome = input("Digite o nome de usuário (ou 'parar' para sair): ").title()
      if nome.lower() == 'parar':
        break
      
      status = input("Selecione o status (1 - Sucesso | 2 - Falha): ")  
      if status == '1':  
        status = 'Sucesso'  
      elif status == '2':  
        status = 'Falha'  
      else:  
        print("Opção inválida, tente novamente: ")  
        continue  
      duracao = int(input("Digite a duração da sessão em minutos: "))
      if duracao < 0:
        print("A duração não pode ser negativa.")
        continue
        
      tuplas = (nome, status, duracao)  
      dados_de_acesso.append(tuplas)
      
    except ValueError:
       print("Digite apenas dados válidos")




