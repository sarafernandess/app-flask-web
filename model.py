from main import db
from datetime import datetime


class Licitacao(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(30), nullable=False)

    comp = db.Column(db.String(50), nullable=True)

    value = db.Column(db.String(50), nullable=True)
