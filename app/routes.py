from flask import Flask, render_template, redirect, url_for, flash, session, request
from app import app
from app import db
from app.models import Product, User
from app.forms import RegistrationForm
from app.forms import LoginForm
from flask_login import login_user, logout_user, login_required


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods= ['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        novo_usuario = User (
            nome = form.nome.data,
            email = form.email.data,
            senhacrip = form.senha.data
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect (url_for('products'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao cadastrar usuário {err}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        logged_user = User.query.filter_by(email=form.email.data).first()
        if logged_user and logged_user.converte_senha(form.senha.data):
            login_user(logged_user)
            flash(f"Sucesso! Seu usuário é {logged_user.nome}", category="success")
            return redirect(url_for('users'))
        else:
            flash("Usuário ou senha incorretos. Por favor, tente novamente.", category="danger")
    return render_template('login.html', form=form)


@app.route('/users')
def users():
    return render_template ('users.html')



@app.route('/products')
@login_required  # proteger rotas específicas
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/logout')
def logout():
    logout_user()
    flash('Você saiu com sucesso.', category='info')
    return redirect(url_for('index'))

