from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    application.config.from_object(
        "config.DevelopmentConfig")

    from index.index import index_blueprint
    application.register_blueprint(index_blueprint)

    from licitacao.routes import licitacao_blueprint
    application.register_blueprint(licitacao_blueprint)

    db.init_app(application)

    if application.config["TESTING"]:
        with application.app_context():
            db.drop_all()
            db.create_all()


    return application

from model import *

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000)