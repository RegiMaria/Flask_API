from sqlalchemy import create_engine 
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from config import Config  # Importe sua configuração

# Crie a URI do banco de dados PostgreSQL
db_uri = Config.SQLALCHEMY_DATABASE_URI

try:
    # Crie uma engine de conexão
    engine = create_engine(db_uri)

    # Tente conectar
    engine.connect()

    # Se conectado com sucesso, imprima uma mensagem
    print("Conexão bem-sucedida!")

    Session = sessionmaker(bind=engine)
    session = Session()

    session.close()

except OperationalError as e:
    # Se ocorrer um erro de conexão, imprima o erro
    print("Erro de conexão:", e)
