import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
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

    if usuario_id is None:
        g.usuario = None
    else:
        g.usuario = get_db().execute(
            'SELECT * FROM usuario WHERE id = ?', (usuario_id,)
        ).fetchone()

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Nome de usuário é obrigatório.'
        elif not password:
            error = 'Senha é obrigatória.'
        elif db.execute('SELECT id FROM usuario WHERE username = ?', (username,)).fetchone() is not None:
            error = f'Usuário {username} já existe.'

        if error is None:
            db.execute(
                'INSERT INTO usuario (username, password_hash) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            flash('Usuário registrado com sucesso! Faça o login.')
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        usuario = db.execute(
            'SELECT * FROM usuario WHERE username = ?', (username,)
        ).fetchone()

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
        error = None

        if not username:
            error = 'Nome de usuário é obrigatório.'
        elif username != g.usuario['username'] and \
             db.execute('SELECT id FROM usuario WHERE username = ?', (username,)).fetchone() is not None:
            error = f'O nome de usuário "{username}" já está em uso.'
        
        if error is None:
            db.execute(
                'UPDATE usuario SET username = ? WHERE id = ?',
                (username, g.usuario['id'])
            )
            db.commit()
            g.usuario = db.execute('SELECT * FROM usuario WHERE id = ?', (g.usuario['id'],)).fetchone()
            flash('Nome de usuário atualizado!')
            return redirect(url_for('auth.perfil'))

        flash(error)
    
    return render_template('auth/perfil.html')

@bp.route('/perfil/deletar', methods=('POST',))
@login_required
def deletar_perfil():
    db = get_db()
    db.execute('DELETE FROM usuario WHERE id = ?', (g.usuario['id'],))
    db.commit()
    session.clear() # Desloga o usuário
    flash('Sua conta foi deletada.')
    return redirect(url_for('auth.register'))