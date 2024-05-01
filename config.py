import os
class Config:
    SECRET_KEY = '8a58c59683d5302432114789cc17e722'        #os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://regimaria:pedagogia@localhost:5432/feedsupplay'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    