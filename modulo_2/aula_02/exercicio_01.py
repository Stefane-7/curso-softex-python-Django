"""Exercício 1: Filtragem e Análise de Dados de Vendas
Você tem uma lista de vendas, onde cada venda é uma tupla (nome_do_produto, valor,
quantidade).

1. Crie uma nova lista chamada vendas_filtradas contendo apenas as tuplas onde o valor
total da venda (valor * quantidade) é maior que 100.

2. Crie um conjunto com todos os nomes de produtos únicos da lista original.

O que vai entrar:
vendas = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1), ("Fone", 45, 1),
("Webcam", 75.20, 2)]

A saída esperada:
Vendas filtradas (valor total >= 100):
[('Teclado', 50, 2), ('Mouse', 25.5, 4), ('Monitor', 300, 1), ('Webcam', 75.2, 2)]
Produtos únicos:
{'Monitor', 'Fone', 'Mouse', 'Teclado', 'Webcam'}"""

vendas = [
    ("Teclado", 50, 2),
    ("Mouse", 25.50, 4),
    ("Monitor", 300, 1),
    ("Fone", 45, 1),
    ("Webcam", 75.20, 2),
]

vendas_filtradas = []
produtos_unicos = set()