import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2.extras # importante para acessar colunas por nome
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.usuario is None:
            flash('Você precisa estar logado para ver esta página.')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    usuario_id = session.get('usuario_id')
    g.usuario = None
    if usuario_id is not None:
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('SELECT * FROM usuario WHERE id = %s', (usuario_id,))
        g.usuario = cursor.fetchone()
        cursor.close()

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        error = None

        if not username:
            error = 'Nome de usuário é obrigatório.'
        elif not password:
            error = 'Senha é obrigatória.'
        
        if error is None:
            try:
                cursor.execute(
                    'INSERT INTO usuario (username, password_hash) VALUES (%s, %s)',
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f'Usuário {username} já existe.'
                db.rollback() # desfaz a transação em caso de erro
            else:
                flash('Usuário registrado com sucesso! Faça o login.')
                cursor.close()
                return redirect(url_for('auth.login'))
        
        flash(error)
        cursor.close()
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        error = None
        
        cursor.execute('SELECT * FROM usuario WHERE username = %s', (username,))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario is None:
            error = 'Nome de usuário incorreto.'
        elif not check_password_hash(usuario['password_hash'], password):
            error = 'Senha incorreta.'

        if error is None:
            session.clear()
            session['usuario_id'] = usuario['id']
            flash('Login realizado com sucesso!')
            return redirect(url_for('listas.index'))

        flash(error)
        
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Você foi desconectado.')
    return redirect(url_for('auth.login'))

@bp.route('/perfil', methods=('GET', 'POST'))
@login_required
def perfil():
    if request.method == 'POST':
        username = request.form['username']
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        error = None

        if not username:
            error = 'Nome de usuário é obrigatório.'
        
        if error is None:
            try:
                cursor.execute(
                    'UPDATE usuario SET username = %s WHERE id = %s',
                    (username, g.usuario['id'])
                )
                db.commit()
            except db.IntegrityError:
                error = f'O nome de usuário "{username}" já está em uso.'
                db.rollback()
            else:
                flash('Nome de usuário atualizado!')
                cursor.close()
                return redirect(url_for('auth.perfil'))

        flash(error)
        cursor.close()
    return render_template('auth/perfil.html')

@bp.route('/perfil/deletar', methods=('POST',))
@login_required
def deletar_perfil():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM usuario WHERE id = %s', (g.usuario['id'],))
    db.commit()
    cursor.close()
    session.clear()
    flash('Sua conta foi deletada.')
    return redirect(url_for('auth.register'))