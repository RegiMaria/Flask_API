from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class Cadastroform(FlaskForm):
    nome = StringField(label='Nome completo')
    email = StringField(label='Email')
    senha_hash = PasswordField(label='Senha', validators=[DataRequired()])
    submit = SubmitField(label='Cadastrar')