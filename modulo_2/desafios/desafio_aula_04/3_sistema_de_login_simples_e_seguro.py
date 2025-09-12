"""Crie um sistema de cadastro e login de usuários. Ele deve:
● Permitir que um usuário se registre com um nome e senha.
● Validar a senha para garantir que ela seja segura (com pelo menos 8 caracteres e uma
mistura de letras e números).
● Permitir que o usuário faça login digitando seu nome e senha.
● Informar se o login foi bem-sucedido ou falhou."""

def cadastrar_usuario():
    nome = input("Cadastre seu nome de usuário: ").lower()
    senha = input("Cadastre sua senha: ").strip()

    while True:
        tem_letra = False
        tem_numero = False

        for caractere in senha:
            if caractere.isalpha():
                tem_letra = True
            if caractere.isdigit():
                tem_numero = True

        if len(senha) >= 8 and tem_letra and tem_numero:
            print("Cadastro realizado com sucesso!")
            return nome, senha
        else:
            print("A senha deve ter pelo menos 8 caracteres, incluindo letras e números.")
            senha = input("Cadastre sua senha novamente: ").strip()


def login_usuario(nome_salvo, senha_salva):
    while True:
        nome = input("Digite seu nome de usuário: ").lower()
        senha = input("Digite sua senha: ").strip()

        if nome == nome_salvo and senha == senha_salva:
            print("Login bem-sucedido!!!")
            return True
        else:
            print("Login ou senha incorretos. Tente novamente.")


def sistema():
    nome, senha = cadastrar_usuario
    login_usuario(nome, senha)          # 


sistema()
