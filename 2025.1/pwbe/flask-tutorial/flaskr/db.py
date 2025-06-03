import sqlite3
from datetime import datetime
import click
from flask import current_app, g

def get_db():
    """Conecta-se ao banco de dados configurado, criando uma nova conexão se não existir para a requisição atual."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """Fecha a conexão com o banco de dados se ela existir."""
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """Limpa os dados existentes e cria novas tabelas."""
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Comando de linha para inicializar o banco de dados."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """Registra funções de banco de dados com a aplicação Flask."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode()))