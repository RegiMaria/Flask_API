Esse documento contém alguns comandos utilizados no Flask-Migrate e no SQLAlchemy:
<h2>Comandos do SQLAlchemy:</h2>

**Deletando itens da tabela produtos:**

from app import db

from app.models import Product

 app.app_context().push()

Product_id = 3

product_to_delete = db.session.get(Product, product_id)

db.session.delete(product_to_delete)

db.session.commit()


**Adicionando itens a tabela Produtos:**

from app import db

from app.models import Product

 app.app_context().push()
 
new_product = Product(type='Especial', name='Novo Produto',  corante='sim', transgênico='Transgênico', aditivos_quimicos='Aditivos', organismo_geneticament
e_modificado='OGM')

Adicionar a nova instância à sessão do banco de dados:
db.session.add(new_product)

db.session.commit()

**Editando itens na Tabela Produtos:

from app import db
from app.models import Product
app.app_context().push()

product_id = 4
product_to_edit = Product.query.get(product_id)

product_to_edit.type = 'Novo Tipo'
product_to_edit.name = 'Novo Nome'
product_to_edit.corante = 'Não'
db.session.commit()

**Editando conteúdo de uma coluna específica:**
from app import db
from app.models import Product
app.app_context().push()

product_id= 5
new_aditivos_quimicos = 'Novo valor para aditivos químicos'
product_to_edit = Product.query.get(product_id)
product_to_edit.aditivos_quimicos = new_aditivos_quimicos -Atulaiza o conteúdo.
db.session.commit()

**Consultando Registros da tabela Products:**
from app import db
from app.models import Product
app.app_context().push()
- Específico pelo ID:

product_id = 1

product = Product.query.get(product_id)

Consulta produtos com tipo:
products_filtered = Product.query.filter_by(type='Tipo').all()


<h2>Flask-Migrate (Alembic)</h2>
**Cria migração:**

flask db migrate -m "Descrição da migração"

**Aplica migração pendente:**

flask db upgrade

**Desfaz a última migração:**

flask db downgrade

**Gerando chave aleatória (secret_key)em Flask:**

 import secrets

secret_key = secrets.token_hex(16)

 print(secret_key)
 ou
 print(app.config['SECRET_KEY'])

**Secret_key no terminal python:**

**Gerando Secret_Key:**
import os
os.unrandom(12).hex()
**Armazenando a 'secret_key' numa variável de ambiente:**
setx FLASK_SECRET_KEY "sua_chave_secreta_aqui"

**Recuperando a secret_key no arquivo de configuração do flask:**

import os

class Config:

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


