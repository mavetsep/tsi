import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # garantir q pasta instance exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass # pasta já existe

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import listas
    app.register_blueprint(listas.bp)
    app.add_url_rule('/', endpoint='listas.index')

    from . import tarefas
    app.register_blueprint(tarefas.bp)

    return app