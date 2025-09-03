"""Exercício 1: Validação de E-mail Básico
Crie um programa que simula uma validação simples de endereço de e-mail.
1. Defina uma variável para um e-mail correto predefinido (exemplo:
"usuario@dominio.com").
2. Defina uma senha de acesso.
3. O programa deve pedir a senha ao usuário. Use um while loop para garantir que o
acesso só ocorra após a senha correta ser digitada.
4. Após o login, peça ao usuário para digitar um e-mail para validação.
5. O programa deve verificar se o e-mail digitado contém o caractere "@" e se o e-mail
termina com ".com".
6. Use uma estrutura if para checar as duas condições. Use o operador and para combinar
as verificações.
7. Se ambas as condições forem verdadeiras, exiba a mensagem: "E-mail válido!". Se uma
ou ambas as condições forem falsas, exiba a mensagem: "E-mail inválido.".
8. O programa deve perguntar se o usuário quer validar outro e-mail. Se a resposta for
"sim", o processo deve se repetir. Se for "não", o programa deve encerrar."""

e_mail = "exercicio01_aula_08@gmail.com"
senha = "taficandodificil123"

while True:
   entrada = input("Digite sua senha: ").lower()
   if entrada == senha:
     break
   else:
     print("Por favor digite a senha correta!")
while True:
   email_usuario = input("Digite seu e-mail: ").lower()
   if "@" in email_usuario and email_usuario.endswith(".com"):
     print("E-mail válido!")
   else:
     print("E-mail inválido!")
   continuar = input("Deseja válidar outro e-mail? (sim/não): ").lower()
   if continuar != "sim":
     print("Encerrando programa...")
     break

    
  