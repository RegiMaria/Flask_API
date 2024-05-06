from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    def validate_nome(self, check_user):
        user = User.query.filter_by(nome=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de usuário")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já existe! Cadastre outro email")

    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe! Cadastre outra senha")

    nome = StringField(label='Nome completo', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    senha = PasswordField(label='Senha', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label='Cadastrar')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])
    submit = SubmitField(label='Log In')