proibida = "spoiler"
while True:
   palavra = input("Digite uma palvra: ")
   palavra1 = palavra.lower()
   if proibida in palavra1:
     print("Por favor digite novamente.")
   else:
    print('Ok')
    break