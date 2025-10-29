def transpor_matriz(matriz):
    transposta = [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]
    return transposta

# Exemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpor_matriz(matriz))
