senha = input('Digite uma senha: ')

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_simbolo = False 

i = 0 
while i < len(senha): 
    caractere = senha[i]
    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower:
        tem_minuscula = True   
    elif caractere.isdigit():
        tem_numero = True 
    elif not caractere.isalnum:
        tem_simbolo = True

        

   