# todolist postgres

## mesma coisa da outra todolist mas agora usando postgres

# 1. navegue para a pasta do projeto
cd todolistpostgres

# 2. crie um ambiente virtual
python -m venv .venv

# 3. ative o ambiente virtual
.venv\Scripts\activate

# 4. instale as dependências do projeto
pip install -r requirements.txt

# 5. configuração do bd no pgAdmin4
abra o pgAdmin4 e conecte ao servidor local.

crie o usuario da aplicacao (todolist_user):

botão direito do mouse em login/group roles > create > login/group role
general, em name, digite todolist_user.
definition, defina uma senha para o usuario. 
privileges, marcar a opção "can login?" com yes.
save.

crie o bd(todolist_db):

botão direito do mouse em databases > create > database
Na aba General:
database, digite todolist_db.
owner, selecione o usuario todolist_user que você acabou de criar.
save.

# 6. configuração e execução

configure a string de conexão:

abra o projeto no editor de código
abra o arquivo flaskr/__init__.py.
encontre a linha da variável POSTGRES_DB_URI e substitua o placeholder da senha pela mesma senha que você definiu para o usuario todolist_user.

# exemplo no meu projeto:
      POSTGRES_DB_URI='postgresql://todolist_user:senha1234@localhost:5432/todolist_db'
## altere o 'senha1234' para a que você colocou

# 7. inicie o bd

com o ambiente virtual ativo execute o comando a seguir no terminal

flask --app flaskr init-db

depois, execute a aplicação

flask --app flaskr run --debug