from app import db, login_manager
from app import Bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    corante = db.Column(db.Text, nullable=True)
    transgênico = db.Column(db.Text, nullable=True)
    aditivos_quimicos_sinteticos = db.Column(db.Text, nullable=True)
    organismos_geneticamente_modificados = db.Column(db.Text, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # Chave estrangeira que referencia o usuário que adicionou o produto
    owner = db.relationship("User", back_populates="products")  # Relacionamento com o usuário

    def __repr__(self):
        return f"Product {self.name}"
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), unique=True, nullable=False)  #senha_hash
    products = db.relationship("Product", back_populates="owner")  # Relacionamento com os produtos

    @property
    def senhacrip(self):
        return self.senhacrip
    
    @senhacrip.setter
    def senhacrip(self, senha_Texto):
        self.senha = Bcrypt.generate_password_hash(senha_Texto).decode('utf-8')
    
    def converte_senha(self, senha_texto_claro):
        return Bcrypt.check_password_hash(self.senha, senha_texto_claro)
