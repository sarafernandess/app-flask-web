from flask import redirect, render_template, url_for

from licitacao import licitacao_blueprint
from licitacao.forms import LicitacaoForm
from main import db

from model import Licitacao


@licitacao_blueprint.route("/", methods=["GET"])
def list_licitacaoes():
    return render_template(
        template_name_or_list="licitacao/list.html",
        licitacao=Licitacao.query.all())


@licitacao_blueprint.route("/new", methods=["GET", "POST"])
def new_licitacao():
    form = LicitacaoForm()

    if form.validate_on_submit():
        licitacao = Licitacao(id=int(form.id.data), title=str(form.title.data), comp=str(form.comp.data), value=str(form.value.data))
        db.session.add(licitacao)
        db.session.commit()
        return "Adicionado!"

    return render_template("licitacao/new.html", form=form)