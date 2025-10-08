/*      
           Exercício 1: Relacionamento Um para Muitos (1:N)

Cenário: Uma biblioteca precisa gerenciar livros e autores.

Passo 1: Inserção de Dados

● Tabela autores:

○ Atributos: id_autor, nome, nacionalidade.

○ Pedidos de Inserção:

■ Insira 2 autores.

● Tabela livros:

○ Atributos: id_livro, titulo, ano_publicacao, id_autor (chave estrangeira).

○ Pedidos de Inserção:

■ Insira 3 livros, associando-os aos autores que você criou.

Passo 2: Pedidos de Consulta

1. Consulta sem JOIN: Selecione o título de todos os livros e o ano de publicação.

2. Consulta com JOIN e filtro: Mostre o título de cada livro e o nome do seu autor.

3. Consulta com JOIN e filtro WHERE: Mostre os títulos dos livros e os nomes dos

autores com a nacionalidade 'Britânica'.

4. Consulta com COUNT: Conte quantos livros cada autor escreveu.*/ 

CREATE TABLE autores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT
);

CREATE TABLE livros(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
);

INSERT INTO autores(nome, nacionalidade) VALUES ('Machado de Assis', 'Brasileiro');
INSERT INTO autores(nome, nacionalidade) VALUES ('Clarice Lispector', 'Brasileira');
INSERT INTO autores(nome, nacionalidade) VALUES ('William Shakespeare', 'Britânico');

INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES ('Memórias Póstumas De Brás Cuba', 1881, 1);
INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES ('Dom Casmurro', 1899, 1);
INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES ('Perto Do Coração Selvagem ', 1943, 2);
INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES ('Romeu e Julieta', 1597, 3);

SELECT * FROM livros;
SELECT titulo, ano_publicacao FROM livros;

SELECT livros.titulo, autores.nome FROM livros
INNER JOIN autores ON livros.id_autor = autores.id;

SELECT livros.titulo, autores.nome FROM livros
INNER JOIN autores ON livros.id_autor = autores.id
WHERE nacionalidade = 'Britânico';

SELECT autores.nome, COUNT(livros.id) AS QTD_Livros
FROM autores
INNER JOIN livros ON livros.id_autor = autores.id
GROUP BY autores.nome;
