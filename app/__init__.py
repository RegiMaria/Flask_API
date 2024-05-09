from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
Bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view='login'
login_manager.login_message= 'Por favor, realize o login'
login_manager.login_message_category='info'
from app import routes, models
from app import api_routes