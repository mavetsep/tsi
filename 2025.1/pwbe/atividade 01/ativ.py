# ===============================================
# atividade 1 - paulo ricardo estevam batalha
# ===============================================

# anotaçoes importantes:
# criar o ambiente virtual:
# python -m venv .venv 

# ativar o venv:
# .venv\Scripts\activate 

# instalar Flask:
# pip install flask

# rodar servidor:
# flask --app ativ run --debug

# arquivo de requisitos pro git 
# pip freeze > requirements.txt

# deactivate (desativa o venv)

# criar aplicaçao do zero

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import flash


app = Flask(__name__)
app.secret_key = 'paulo123' # senha do session
app.config['SESSION_COOKIE_SECURE'] = True 
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# dados mockados

# usuarios e senhas
usuarios = {
    'paulo': '123',  
    'ricardo': '456',
    'estevam': '789',
    'batalha': 'abc',
}

musicas = {
    'paulo': ['electric feel', 'everlong'],
    'ricardo': ['reptilia', 'just like heaven'],
    'estevam': ['stairway to heaven', 'iron man'],
    'batalha': ['hungry like the wolf', 'instant crush'],
}

# forms de login

@app.route('/')
def index():
    if 'usuario' in session:
        flash('Você já está logado!', 'info')
        return redirect(url_for('bem_vindo'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # post
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()  # valor do campo usuario
        senha = request.form.get('senha', '').strip()      # valor do campo senha
        
        if not usuario or not senha:
            return redirect(url_for('erro_login', motivo='campos_vazios'))
        
        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario  # armazena o usuario na sessao 
            flash(f'Bem-vindo, {usuario}!', 'success')
            return redirect(url_for('bem_vindo'))
        
        # redireciona para a página de erro
        return redirect(url_for('erro_login', motivo='credenciais_invalidas'))
    
    # get
    return render_template('index.html')

# erro de login 

@app.route('/erro')
def erro_login():
    motivo = request.args.get('motivo', 'credenciais_invalidas')
    
    if motivo == 'campos_vazios':
        mensagem = "Por favor, preencha todos os campos"
    else:
        mensagem = "Usuário ou senha inválidos"
    
    return render_template('erro.html', mensagem=mensagem)

# boas vindas

@app.route('/bem-vindo')
def bem_vindo():
    if 'usuario' not in session:
        flash('Por favor, faça login primeiro', 'warning')
        return redirect(url_for('index'))
    return render_template('bem_vindo.html', nome=session['usuario'])

# musicas favoritas

@app.route('/musicas')
def listar_musicas():
    if 'usuario' not in session:
        flash('Por favor, faça login primeiro', 'warning')
        return redirect(url_for('index'))
    
    user_musicas = musicas.get(session['usuario'], [])
    return render_template('musicas.html', musicas=user_musicas)

# adicionar musicas a lista de musicas favoritas

@app.route('/musicas/adicionar', methods=['POST'])
def adicionar_musica():
    if 'usuario' not in session:
        flash('Por favor, faça login primeiro', 'warning')
        return redirect(url_for('index'))
    
    nova_musica = request.form.get('musica', '').strip()
    if not nova_musica:
        flash('Por favor, digite o nome da música', 'error')
        return redirect(url_for('listar_musicas'))
    
    if nova_musica in musicas[session['usuario']]:
        flash('Esta música já está na sua lista', 'warning')
    else:
        musicas[session['usuario']].append(nova_musica)
        flash('Música adicionada com sucesso!', 'success')
    
    return redirect(url_for('listar_musicas'))

# editar musica especifica

@app.route('/musicas/editar/<int:index>', methods=['GET', 'POST'])
def editar_musica(index):
    if 'usuario' not in session:
        flash('Por favor, faça login primeiro', 'warning')
        return redirect(url_for('index'))
    
    user_musicas = musicas.get(session['usuario'], [])
    
    if index < 0 or index >= len(user_musicas):
        flash('Música não encontrada', 'error')
        return redirect(url_for('listar_musicas'))
    
    if request.method == 'POST':
        nova_musica = request.form.get('musica', '').strip()
        if not nova_musica:
            flash('Por favor, digite o nome da música', 'error')
            return redirect(url_for('editar_musica', index=index))
        
        if nova_musica in user_musicas:
            flash('Esta música já está na sua lista', 'warning')
        else:
            user_musicas[index] = nova_musica
            flash('Música atualizada com sucesso!', 'success')
            return redirect(url_for('listar_musicas'))
    
    return render_template('editar_musica.html', 
                         musica=user_musicas[index], 
                         index=index)

# remover musica especifica

@app.route('/musicas/remover/<int:index>')
def remover_musica(index):
    if 'usuario' not in session:
        flash('Por favor, faça login primeiro', 'warning')
        return redirect(url_for('index'))
    
    user_musicas = musicas.get(session['usuario'], [])
    
    if index < 0 or index >= len(user_musicas):
        flash('Música não encontrada', 'error')
    else:
        removed = user_musicas.pop(index)
        flash(f'Música "{removed}" removida com sucesso!', 'success')
    
    return redirect(url_for('listar_musicas'))

# logout

@app.route('/logout')
def logout():
    if 'usuario' in session:
        usuario = session.pop('usuario')
        flash(f'Até logo, {usuario}! Você foi desconectado.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# 1 criar uma aplicação do zero;
# 2 anotar comandos que sabemos ou achar que vão se repetir e que vamos precisar;
# requisitos:
# página index para boas vindas e form de login.
# que dentro do código vocês, dicionário que tenha nomes de usuário e senhas associados (mocket data)
# fazer o login validando com a lista mencionada acima
# se o login for válido, redirecionar para uma página de boas vindas com o nome do usuário logado.
# se o login for inválido, redirecionar para uma página de erro com a mensagem de erro ou volta para o login com a mensagem (login e senha invalidos).
# com o usuário logado, eu quero poder ter um menu para acessar a lista de músicas preferidas
# manipular a lista de músicas preferidas (adicionar, remover, editar, listar)
# sair da sessão e volta para o login ou uma tela especifica do index caso nao faça o login no index.