usuario = input("digite sua idade:")
num = int(usuario)
if num <= 12:
    print("criança")
elif num >= 13 and num <= 17:
    print("adolescente")
elif num >= 18 and num <= 59:
    print("adulto")