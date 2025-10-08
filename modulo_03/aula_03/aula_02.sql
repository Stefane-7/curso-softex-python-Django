CREATE TABLE usuarioss(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE cursos(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

CREATE TABLE usuarios_curso(
    id_usuario INTEGER,
    id_curso INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarioss(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

INSERT INTO usuarioss(nome) VALUES ('João'), ('Pedro'), ('Maria'), ('Carol');

INSERT INTO cursos(titulo) VALUES ('Backend'), ('Frontend');

INSERT INTO usuarios_curso(id_usuario, id_curso) VALUES (1,1), (1,2), (2,1), (3,1);
INSERT INTO usuarios_curso(id_usuario, id_curso) VALUES (4,2);
SELECT * FROM usuarioss;
SELECT * FROM cursos;
SELECT * FROM usuarios_curso;

SELECT usuarioss.nome , cursos.titulo FROM usuarios_curso
INNER JOIN usuarioss ON usuarios_curso.id_curso = usuarioss.id
INNER JOIN cursos ON usuarios_curso.id_curso = cursos.id;

SELECT count(nome) from usuarioss WHERE nome = 'Carol';

SELECT COUNT(usuarioss.nome) AS QTD_alunos, cursos.titulo FROM usuarios_curso
INNER JOIN usuarioss ON usuarios_curso.id_curso = usuarioss.id
INNER JOIN cursos ON usuarios_curso.id_curso = cursos.id
GROUP BY cursos.titulo;

SELECT COUNT(usuarioss.nome) AS QTD_alunos, cursos.titulo FROM usuarios_curso
INNER JOIN usuarioss ON usuarios_curso.id_curso = usuarioss.id
INNER JOIN cursos ON usuarios_curso.id_curso = cursos.id
GROUP BY cursos.titulo
HAVING COUNT(usuarios.nome) > 2;

