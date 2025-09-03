palavra = input("digite uma palavra: ").lower()
while True:
    if len(palavra) < 3:
        print('a palavra deve ter no minimo 3 caracteres.')
    elif palavra[0] != "p":
      print("A palavra deve comecar com 'P'.")

    elif palavra[len(palavra) - 1] != "s":
        print("A palavra precisa terminar com 'S'")  

    elif "i" not in palavra:
        print("A palavra de conte a letra 'I'") 

    elif "m"in palavra or "n" in palavra:
        print("A palavra nao deve conter 'M' nem 'N' .") 
    else:
        print(f"A palavra '{palavra}' atende tdas as condições!")
        break          