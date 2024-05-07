from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
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

    nome = StringField(label='Nome completo', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    senha = PasswordField(label='Senha', validators=[DataRequired(), Length(min=4, message="A senha deve ter no mínimo 4 caracteres.")])
    submit = SubmitField(label='Cadastrar')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


class ProductForm(FlaskForm):
    type = StringField('Tipo', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "Standart, especial, premium, super premium, natural ..."})
    name = StringField('Nome', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "Marca"})
    corante = SelectField('Corante', choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não declarado pelo fabricante', 'Não declarado pelo fabricante')])
    transgenico = SelectField('Transgênico', choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não declarado pelo fabricante', 'Não declarado pelo fabricante')])
    aditivos_quimicos_sinteticos = TextAreaField('Aditivos Químicos Sintéticos')
    organismos_geneticamente_modificados = TextAreaField('Organismos Geneticamente Modificados')
    submit = SubmitField('Cadastrar')