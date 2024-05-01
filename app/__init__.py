from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager= LoginManager()
migrate = Migrate(app, db)
login_manager.init_app(app)


from app.models import User 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes, models, api_routes