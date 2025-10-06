-- Active: 1759754172922@@127.0.0.1@3306
CREATE TABLE usuarios(id INTEGER PRIMARY KEY, primeiro_nome TEXT NOT NULL, sobrenome TEXT NOT NULL, email TEXT NOT NULL, senha TEXT NOT NULL);
CREATE TABLE postagens(id INTEGER PRIMARY KEY, titulo TEXT NOT NULL, postagem TEXT, id_autor INTEGER);

INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('João', 'Carlos de Albuquerque', 'algumacoisa@gmail.com', '123456');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Maria', 'Alencar', 'algumacoisa_2@gmail.com', '7891011');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Clara', 'Almeida de Linda', 'algumacoisa_3@gmail.com', '121314');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Kaio', 'Oliveira Alves', 'algumacoisa_4@gmail.com', '151617');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Joana', 'Santos Silva', 'algumacoisa_5@gmail.com', '181920');

SELECT * FROM usuarios;


INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('alguem',  'blablabla', 1);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('algo', 'lllallall', 2);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('aaaa', 'não sei o que lá', 3);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('bbbbb', 'uma postagem legal aqui', 4);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('cccccc', 'sem idéias aqui', 5);

SELECT * FROM postagens;