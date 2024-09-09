from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Modelo do banco de dados
class Musica(db.Model):
    id_musica = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    duracao = db.Column(db.Float, nullable=False)
    compositor = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Musica {self.titulo}>'


# Criar o banco de dados
with app.app_context():
    db.create_all()


# Rota para exibir o formulário HTML e as músicas cadastradas
@app.route('/')
def index():
    musicas = Musica.query.all()
    return render_template('index.html', musicas=musicas)


# Rota para adicionar nova música
@app.route('/add', methods=['POST'])
def add_musica():
    titulo = request.form['titulo']
    duracao = request.form['duracao']
    compositor = request.form['compositor']
    album = request.form['album']

    nova_musica = Musica(titulo=titulo, duracao=duracao, compositor=compositor, album=album)

    db.session.add(nova_musica)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

