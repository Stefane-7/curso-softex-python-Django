registros_acessos = []
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
      registros_acessos.append(tuplas)
      
    except ValueError:
      print("Erro: a duração deve ser um número inteiro válido.")

total = 0
for nome, status, duracao in registros_acessos:
  if status == "Sucesso":
    total += duracao

usuarios_bem_sucedidos = set()
for nome, status, tempo in registros_acessos:
  if status == "Sucesso":
    usuarios_bem_sucedidos.add(nome)
  
print("Registros de acessos: ")
print(dados_de_acesso)

print("\nUsuarios com ao menos um login bem-sucedido: ")
print(usuarios_bem_sucedidos)

print("\nTempo total das sessões bem-sucedidas: ")
print(f"\nTempo total das sessões bem-sucedidas: {total} minutos")




