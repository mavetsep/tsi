import psycopg2
import psycopg2.extras # dicionarios em vez de tuplas.

import click
from flask import current_app, g

def get_db():
    """abre uma nova conexao com o bd se nao tiver uma pra a requisicao atual."""
    if 'db' not in g:
        # pega a URI de conexao da configuracao do app.
        db_uri = current_app.config['POSTGRES_DB_URI']
        # estabelece a conexao.
        g.db = psycopg2.connect(db_uri)
    return g.db

def close_db(e=None):
    """fecha a conexao com o bd, se ela existir."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """limpa os dados existentes e cria novas tabelas a partir do schema.sql."""
    db = get_db()
    # cursor psycopg2 para executar comandos
    cursor = db.cursor()

    with current_app.open_resource('schema.sql') as f:
        cursor.execute(f.read().decode('utf8'))
    
    # confirma as alteracoes no banco de dados.
    db.commit()
    cursor.close()


@click.command('init-db')
def init_db_command():
    """define o comando de terminal 'flask init-db'."""
    init_db()
    click.echo('Banco de dados inicializado.')

def init_app(app):
    # close_db seja chamado dps de cada requisicao.
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)