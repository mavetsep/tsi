from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
import psycopg2.extras
from .auth import login_required
from .db import get_db

bp = Blueprint('listas', __name__, url_prefix='/listas')

def get_lista_atual(id_lista, check_autor=True):
    db = get_db()
    cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(
        'SELECT l.id, l.titulo, l.usuario_id, l.criada_em FROM lista_tarefas l WHERE l.id = %s',
        (id_lista,)
    )
    lista = cursor.fetchone()
    cursor.close()

    if lista is None:
        abort(404, f"Lista com id {id_lista} não existe.")

    if check_autor and lista['usuario_id'] != g.usuario['id']:
        abort(403)
    
    return lista

@bp.route('/')
@login_required
def index():
    db = get_db()
    cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(
        'SELECT id, titulo, criada_em FROM lista_tarefas WHERE usuario_id = %s ORDER BY criada_em DESC',
        (g.usuario['id'],)
    )
    minhas_listas = cursor.fetchall()
    cursor.close()
    return render_template('listas/index.html', listas=minhas_listas)

@bp.route('/criar', methods=('GET', 'POST'))
@login_required
def criar_lista():
    if request.method == 'POST':
        titulo = request.form['titulo']
        error = None

        if not titulo:
            error = 'Título é obrigatório.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO lista_tarefas (titulo, usuario_id) VALUES (%s, %s)',
                (titulo, g.usuario['id'])
            )
            db.commit()
            cursor.close()
            flash('Lista criada!')
            return redirect(url_for('listas.index'))

    return render_template('listas/c.html')

@bp.route('/<int:id_lista>/detalhes')
@login_required
def detalhes_lista(id_lista):
    lista = get_lista_atual(id_lista)
    db = get_db()
    cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(
        'SELECT id, descricao_tarefa, completada FROM tarefa WHERE lista_id = %s ORDER BY criada_em ASC',
        (id_lista,)
    )
    tarefas_da_lista = cursor.fetchall()
    cursor.close()
    return render_template('listas/dt.html', lista=lista, tarefas=tarefas_da_lista)

@bp.route('/<int:id_lista>/editar', methods=('GET', 'POST'))
@login_required
def editar_lista(id_lista):
    lista = get_lista_atual(id_lista)

    if request.method == 'POST':
        titulo = request.form['titulo']
        error = None

        if not titulo:
            error = 'Título é obrigatório.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                'UPDATE lista_tarefas SET titulo = %s WHERE id = %s AND usuario_id = %s',
                (titulo, id_lista, g.usuario['id'])
            )
            db.commit()
            cursor.close()
            flash('Lista atualizada!')
            return redirect(url_for('listas.index'))

    return render_template('listas/edt.html', lista=lista)

@bp.route('/<int:id_lista>/deletar', methods=('POST',))
@login_required
def deletar_lista(id_lista):
    get_lista_atual(id_lista) # apenas pra checar permissao
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM lista_tarefas WHERE id = %s AND usuario_id = %s', (id_lista, g.usuario['id']))
    db.commit()
    cursor.close()
    flash('Lista deletada.')
    return redirect(url_for('listas.index'))