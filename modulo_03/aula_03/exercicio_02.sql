/*  Exercício 2: Relacionamento Muitos para Muitos (N:N)

Cenário: Uma academia precisa gerenciar alunos e as aulas que eles frequentam.

Passo 1: Inserção de Dados

● Tabela alunos:

○ Atributos: id_aluno, nome, idade.

○ Pedidos de Inserção:

■ Insira 2 alunos.

● Tabela aulas:

○ Atributos: id_aula, nome_aula.

○ Pedidos de Inserção:

■ Insira 3 aulas.

● Tabela alunos_aulas (Tabela de Ligação):

○ Atributos: id_aluno (chave estrangeira), id_aula (chave estrangeira).

○ Pedidos de Inserção:

■ Insira 4 relações para mostrar quais alunos fazem quais aulas.

Passo 2: Pedidos de Consulta

1. Consulta com JOIN: Mostre o nome de cada aluno e os títulos das aulas que ele faz.

2. Consulta com JOIN e COUNT: Conte quantos alunos cada aula tem.

3. Consulta com JOIN e filtro IN: Selecione os nomes dos alunos que frequentam as
aulas com ID 1 ou 3.

4. Consulta com JOIN e filtro WHERE: Selecione o nome de todos os alunos que fazem a
aula 'Zumba'.*/