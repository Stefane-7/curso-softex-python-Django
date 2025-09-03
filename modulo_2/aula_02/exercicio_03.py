"""        Exercício 3: Sistema de Login

Você tem uma lista de tuplas, onde cada tupla é um registro de acesso (usuario, status_login).
O status_login pode ser 'sucesso' ou 'falha'.

Usando laços de repetição e condicionais, identifique e imprima:

-1. O nome dos usuários que tiveram pelo menos um login bem-sucedido.

-2. O nome dos usuários que tiveram somente logins com falha.

O que vai entrar:
acessos = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"),
("Ana", "falha")]

A saída esperada:
Usuários com pelo menos um login bem-sucedido:
{'Maria', 'Pedro'}
Usuários que tiveram somente logins com falha:
{'Ana'}"""
print("########### exercicio 03 ###########")
acessos = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"),
("Ana", "falha")]

usuarios_bem_sucedido = set()
usuario_mal_sucedido = set()

for usuario, status in acessos:
    if status == "sucesso":
        usuarios_bem_sucedido.add(usuario)
    elif status == "falha":
        usuario_mal_sucedido.add(usuario)   
apenas_falha = usuario_mal_sucedido.difference(usuarios_bem_sucedido)        

print("Usuários com ao menos um login bem-sucedido: ")
print(usuarios_bem_sucedido)

print("\nUsuários que tiveram somente logins com falha: ")
print(apenas_falha)