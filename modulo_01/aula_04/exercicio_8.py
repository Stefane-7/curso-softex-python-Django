senha = input('Digite uma senha com letras e números: ')
senha1 = senha.isalnum()
if senha1:
    print("Senha valida!")
else:
    print('Por favor digite uma senha que atenda aos critérios!')    