import os
class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'   #  banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False