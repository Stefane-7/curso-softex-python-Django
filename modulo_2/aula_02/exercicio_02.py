"""Exercício 2: Comparação de Estoque
Você tem o inventário de uma loja em duas listas de tuplas. Cada tupla representa um produto
(nome_do_produto, id).
● estoque_principal: Produtos disponíveis na loja.
● estoque_online: Produtos disponíveis no site.
Usando conjuntos, descubra e imprima:
1. Os produtos que estão disponíveis tanto na loja física quanto no site.
2. Os produtos que estão apenas na loja física.
3. Os produtos que estão apenas no site.
O que vai entrar:
estoque_principal = [("Camiseta", 101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]
A saída esperada:
Produtos disponíveis na loja e no site:
{('Boné', 103), ('Calça', 102)}
Produtos disponíveis apenas na loja física:
{('Camiseta', 101), ('Tênis', 104)}
Produtos disponíveis apenas no site:
{('Camisa Polo', 105), ('Chinelo', 106)}"""