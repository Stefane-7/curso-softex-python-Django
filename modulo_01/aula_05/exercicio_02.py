palavra = input('Digite uma palavra:')
contador_vogais = 0
vogais = "a,e,i,o,u" 
for letra in palavra.lower():
    if letra in vogais:
        contador_vogais += 1
print(f'Apalvra tem {contador_vogais} vogais.')        
      