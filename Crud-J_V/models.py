from database import db

class Editora(db.Model):
    __tablename__ = 'editora'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade

    def __repr__(self):
        return '<Editora {}>'.format(self.nome)



class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key = True)
    editora_id = db.Column(db.Integer, db.ForeignKey('editora.id'))
    titulo = db.Column(db.String(100))
    ano = db.Column(db.Integer)   

    editora = db.relationship('Editora', foreign_keys = editora_id)

    def __init__(self, editora_id, titulo, ano):
        self.editora_id = editora_id
        self.titulo = titulo
        self.ano = ano

    def __repr__(self):
        return '<Livro {}>'.format(self.titulo)
    
class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key = True)
    editora_id = db.Column(db.Integer, db.ForeignKey('editora.id'))
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'))
    data = db.Column(db.Date)

    editora = db.relationship('Editora', foreign_keys = editora_id)
    livro = db.relationship('Livro', foreign_keys = livro_id)

    def __init__(self, editora_id, livro_id, data):
        self.editora_id = editora_id
        self.livro_id = livro_id
        self.data = data

    def __repr__(self):
        return '<Pedido {} - {} - {}>'.format(self.editora.nome, self.livro.titulo, self.data)
    