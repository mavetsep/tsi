from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
from .auth import login_required
from .db import get_db

bp = Blueprint('listas', __name__, url_prefix='/listas')

def get_lista_atual(id_lista, check_autor=True):
    lista = get_db().execute(
        'SELECT l.id, l.titulo, l.usuario_id FROM lista_tarefas l WHERE l.id = ?',
        (id_lista,)
    ).fetchone()

    if lista is None:
        abort(404, f"Lista com id {id_lista} não existe.")

    if check_autor and lista['usuario_id'] != g.usuario['id']:
        abort(403)
    
    return lista

@bp.route('/')
@login_required
def index():
    db = get_db()
    minhas_listas = db.execute(
        'SELECT id, titulo, criada_em FROM lista_tarefas WHERE usuario_id = ? ORDER BY criada_em DESC',
        (g.usuario['id'],)
    ).fetchall()
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
            db.execute(
                'INSERT INTO lista_tarefas (titulo, usuario_id) VALUES (?, ?)',
                (titulo, g.usuario['id'])
            )
            db.commit()
            flash('Lista criada!')
            return redirect(url_for('listas.index'))

    return render_template('listas/c.html')

@bp.route('/<int:id_lista>/detalhes')
@login_required
def detalhes_lista(id_lista):
    lista = get_lista_atual(id_lista)
    db = get_db()
    tarefas_da_lista = db.execute(
        'SELECT id, descricao_tarefa, completada FROM tarefa WHERE lista_id = ? ORDER BY criada_em ASC',
        (id_lista,)
    ).fetchall()
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
            db.execute(
                'UPDATE lista_tarefas SET titulo = ? WHERE id = ? AND usuario_id = ?',
                (titulo, id_lista, g.usuario['id'])
            )
            db.commit()
            flash('Lista atualizada!')
            return redirect(url_for('listas.index'))

    return render_template('listas/edt.html', lista=lista)

@bp.route('/<int:id_lista>/deletar', methods=('POST',))
@login_required
def deletar_lista(id_lista):
    get_lista_atual(id_lista)
    db = get_db()
    db.execute('DELETE FROM lista_tarefas WHERE id = ? AND usuario_id = ?', (id_lista, g.usuario['id']))
    db.commit()
    flash('Lista deletada.')
    return redirect(url_for('listas.index'))