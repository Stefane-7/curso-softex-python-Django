CREATE TABLE professores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunoss(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor  INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
);

INSERT INTO professores(nome) VALUES ('Anderson');
INSERT INTO professores(nome) VALUES ('Fabricio');
SELECT * FROM professores;

INSERT INTO alunoss(nome, id_professor) VALUES ('João', 2);
INSERT INTO alunoss(nome, id_professor) VALUES ('Maria', 2);
INSERT INTO alunoss(nome, id_professor) VALUES ('Julia', 1);
INSERT INTO alunoss(nome, id_professor) VALUES ('Pedro', 1);
DELETE FROM alunos WHERE nome = 'Pedro';
SELECT * FROM alunoss;
SELECT id AS Identificador, nome AS Priemeiro_Nome FROM alunos;

SELECT alunoss.nome AS nome_aluno, professores.nome AS nome_professor
FROM alunoss
INNER JOIN professores ON alunoss.id_professor = professores.id;
DELETE FROM professores WHERE id = 2;
