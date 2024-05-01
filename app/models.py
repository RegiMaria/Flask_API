from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import PasswordField
from wtforms.validators import DataRequired, Email
from sqlalchemy import event
from flask_login import  UserMixin


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    corante = db.Column(db.Text, nullable=True)
    transgênico = db.Column(db.Text, nullable=True)
    aditivos_quimicos = db.Column(db.Text, nullable=True)
    organismo_geneticamente_modificado = db.Column(db.Text, nullable=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)   #senha_hash

    def set_password(self, password):
        self.senha_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha_hash, password)

# Função para truncar automaticamente os dados que excedem o limite
    @staticmethod
    def truncate_long_values_before_insert(mapper, connection, target):
        if len(target.nome) > 50:
            target.nome = target.nome[:50]
        if len(target.email) > 120:
            target.email = target.email[:120]
        if len(target.senha_hash) > 128:
            target.senha_hash = target.senha_hash[:128]

# Adiciona o listener para o evento 'before_insert'
event.listen(User, 'before_insert', User.truncate_long_values_before_insert)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


    # função truncate_long_values_before_insert é definida para verificar os comprimentos
    # dos campos nome, email e senha_hash e truncá-los, se necessário, 
    #antes de realizar a inserção no banco de dados. 
    #Esta função é então associada ao evento before_insert do modelo User usando event.listen.

    # a SENHA do usuário é um hash da senha, uma representação
    # criptograficamente segura e irreversível da senha original.

    # A função 'set_password'  gerar o hash da senha fornecida pelo usuário
    # e armazena em 'senha_hash' do modelo de usuário.
    # Ele utiliza a função 'generate_password_hash' do Werkzeug para calcular o hash da senha.

    # Processo de autenticação de usuário:
    # A função 'check_password' é usada para verificar se a senha fornecida pelo usuário corresponde
    # ao hash armazenado no banco de dados.
    # Ele utiliza a função 'check_password_hash' do Werkzeug para comparar a senha fornecida com
    # o hash armazenado.
    # Se as senhas corresponderem, a função retorna True, indicando que a senha é válida.
    # Se não corresponderem, retorna False, indicando que a senha é inválida.