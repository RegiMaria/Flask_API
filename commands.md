**Instalação dos pacotes:**
flask
flak-sqlalchemy
psycopg2
flask_login
flask-snippets (extensão pra vscode)
flask-wTF
WTForms
flask_bcrypt


1. Teste a conexão com bd postegreSQL
Se "Conexão bem-sucedida!", criar os models.

2. Criando o models no BD:
from app import app
from app import db
app.app_context().push()
app.create_all()

As tabelas podeão ser observadas no próprio banco de dados.

3. Instalar Flask-migrate:
pip install flask-migrate

comandos:
flask db init - inicializa
flask db migrate -m "Initial migration" - criar uma migração inicial com base no estado atual do seu modelo de banco de dados
flask db upgrade - aplica a migração ao BD

4. Criando novo usuario