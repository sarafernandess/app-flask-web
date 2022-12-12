from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class LicitacaoForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    title = StringField("Título", validators=[DataRequired()])
    comp = StringField("Empresa", validators=[DataRequired()])
    value = StringField("Valor", validators=[DataRequired()])
