
from flask import Blueprint

licitacao_blueprint = Blueprint(
    "licitacao_blueprint", __name__, url_prefix="/licitacao")

from .routes import *