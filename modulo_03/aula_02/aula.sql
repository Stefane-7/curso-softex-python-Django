CREATE TABLE alunos(id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTEGER);

INSERT INTO alunos(nome, idade) VALUES ('João', 20);
INSERT INTO alunos(nome, idade) VALUES ('Maria', 22);

SELECT * FROM alunos;