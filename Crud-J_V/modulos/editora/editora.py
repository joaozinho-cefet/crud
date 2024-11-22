from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Editora

bp_editora = Blueprint('editora', __name__, template_folder='templates')

@bp_editora.route('/')
def index():
    dados = Editora.query.all()
    return render_template('editora.html', dados=dados)

@bp_editora.route('/add')
def add():
    return render_template('editora_add.html')

@bp_editora.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if nome and cidade:
        objeto = Editora(nome, cidade)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/editora')
    else:
        flash('Preencha todos os campos!')
        return redirect('/editora/add')
