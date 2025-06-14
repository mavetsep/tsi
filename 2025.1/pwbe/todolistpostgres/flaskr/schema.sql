-- apaga as tabelas se elas ja existirem, prra garantir um comeco limpo.
DROP TABLE IF EXISTS tarefa;
DROP TABLE IF EXISTS lista_tarefas;
DROP TABLE IF EXISTS usuario;

-- cria as tabelas do banco de dados.
CREATE TABLE usuario (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL
);

CREATE TABLE lista_tarefas (
  id SERIAL PRIMARY KEY,
  usuario_id INTEGER NOT NULL,
  titulo TEXT NOT NULL,
  -- funçao NOW() eh padrao do postgres para a data e hora.
  criada_em TIMESTAMP NOT NULL DEFAULT NOW(),
  -- a definição de fk eh a mesma.
  FOREIGN KEY (usuario_id) REFERENCES usuario (id) ON DELETE CASCADE
);

CREATE TABLE tarefa (
  id SERIAL PRIMARY KEY,
  lista_id INTEGER NOT NULL,
  descricao_tarefa TEXT NOT NULL,
  -- postgres boolean verdadeiro (true/false).
  completada BOOLEAN NOT NULL DEFAULT FALSE,
  criada_em TIMESTAMP NOT NULL DEFAULT NOW(),
  FOREIGN KEY (lista_id) REFERENCES lista_tarefas (id) ON DELETE CASCADE
);