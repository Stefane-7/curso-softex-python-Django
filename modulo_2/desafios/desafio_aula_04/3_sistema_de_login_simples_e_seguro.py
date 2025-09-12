"""Crie um sistema de cadastro e login de usuários. Ele deve:
● Permitir que um usuário se registre com um nome e senha.
● Validar a senha para garantir que ela seja segura (com pelo menos 8 caracteres e uma
mistura de letras e números).
● Permitir que o usuário faça login digitando seu nome e senha.
● Informar se o login foi bem-sucedido ou falhou."""

def sistema_login():
  nome_salvo = "programação"
  senha_salva = "python123"
  
  while True:
    nome = input("Digite seu nome de usuario: ").lower()
    senha = input("Digite sua senha: ")
    senha_limpa = senha.strip()
    if nome == nome_salvo:
        if len(senha_limpa) >= 8 and senha_limpa.isalnum():
            if senha_limpa == senha_salva:
              print("Login bem-sucedido!!!")
              return
            else:
                print("Login ou senha incorretos. Tente novamente.")
        else:
          print("Login ou senha incorretos. Tente novamente.")
    else:
      print("Login ou senha incorretos. Tente novamente.")

sistema_login()