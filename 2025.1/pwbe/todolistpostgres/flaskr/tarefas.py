from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
import psycopg2.extras
from .auth import login_required
from .db import get_db
from .listas import get_lista_atual

bp = Blueprint('tarefas', __name__, url_prefix='/tarefas')

def get_tarefa_atual(id_tarefa, check_autor=True):
    db = get_db()
    cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(
        'SELECT t.id, t.descricao_tarefa, t.completada, t.lista_id, l.usuario_id '
        'FROM tarefa t JOIN lista_tarefas l ON t.lista_id = l.id '
        'WHERE t.id = %s',
        (id_tarefa,)
    )
    tarefa = cursor.fetchone()
    cursor.close()

    if tarefa is None:
        abort(404, f"Tarefa com id {id_tarefa} não existe.")

    if check_autor and tarefa['usuario_id'] != g.usuario['id']:
        abort(403)
    
    return tarefa

@bp.route('/lista/<int:id_lista>/criar', methods=('GET', 'POST'))
@login_required
def criar_tarefa(id_lista):
    lista_pai = get_lista_atual(id_lista) 

    if request.method == 'POST':
        descricao = request.form['descricao_tarefa']
        error = None

        if not descricao:
            error = 'Descrição da tarefa é obrigatória.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO tarefa (lista_id, descricao_tarefa) VALUES (%s, %s)',
                (id_lista, descricao)
            )
            db.commit()
            cursor.close()
            flash('Tarefa adicionada!')
            return redirect(url_for('listas.detalhes_lista', id_lista=id_lista))

    return render_template('tarefas/cr.html', lista=lista_pai)

@bp.route('/<int:id_tarefa>/editar', methods=('GET', 'POST'))
@login_required
def editar_tarefa(id_tarefa):
    tarefa = get_tarefa_atual(id_tarefa)

    if request.method == 'POST':
        descricao = request.form['descricao_tarefa']
        completada = 'completada' in request.form 

        error = None
        if not descricao:
            error = 'Descrição é obrigatória.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                'UPDATE tarefa SET descricao_tarefa = %s, completada = %s WHERE id = %s',
                (descricao, completada, id_tarefa)
            )
            db.commit()
            cursor.close()
            flash('Tarefa atualizada!')
            return redirect(url_for('listas.detalhes_lista', id_lista=tarefa['lista_id']))

    return render_template('tarefas/edtr.html', tarefa=tarefa)

@bp.route('/<int:id_tarefa>/deletar', methods=('POST',))
@login_required
def deletar_tarefa(id_tarefa):
    tarefa = get_tarefa_atual(id_tarefa)
    id_lista_pai = tarefa['lista_id']
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM tarefa WHERE id = %s', (id_tarefa,))
    db.commit()
    cursor.close()
    flash('Tarefa deletada.')
    return redirect(url_for('listas.detalhes_lista', id_lista=id_lista_pai))

@bp.route('/<int:id_tarefa>/alternar_status', methods=('POST',))
@login_required
def alternar_status_tarefa(id_tarefa):
    tarefa = get_tarefa_atual(id_tarefa)
    novo_status = not tarefa['completada'] 
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE tarefa SET completada = %s WHERE id = %s',
        (novo_status, id_tarefa)
    )
    db.commit()
    cursor.close()
    
    status_texto = "completa" if novo_status else "pendente"
    flash(f'Tarefa marcada como {status_texto}.')
    return redirect(url_for('listas.detalhes_lista', id_lista=tarefa['lista_id']))