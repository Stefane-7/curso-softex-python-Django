contador = -100000000
for i in range(5):
   numero = int(input(f"Digite {i+1}º numero: "))
   if numero > contador:
      contador = numero
print(f"O maior numero é: {contador}") 