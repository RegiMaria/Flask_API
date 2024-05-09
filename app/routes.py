from flask import Flask, render_template, redirect, url_for, flash, session, request
from app import app
from app import db
from app.models import Product, User
from app.forms import RegistrationForm, ProductForm
from app.forms import LoginForm
from flask import abort
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        novo_usuario = User(
            nome=form.nome.data,
            email=form.email.data,
            senhacrip=form.senha.data
        )
        db.session.add(novo_usuario)
        db.session.commit()
        login_user(novo_usuario)
        return redirect(url_for('users'))
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
    return render_template('users.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Você saiu com sucesso.', category='info')
    return redirect(url_for('index'))


@app.route('/productaddition', methods=['GET', 'POST'])
def product_addition():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            type=form.type.data,
            corante=form.corante.data,
            transgenico=form.transgenico.data,
            aditivos_quimicos_sinteticos=form.aditivos_quimicos_sinteticos.data,  # Correção aqui
            organismos_geneticamente_modificados=form.organismos_geneticamente_modificados.data,
            owner_id=current_user.id  # Correção aqui
        )
        db.session.add(product)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('product_confirmation',
                                product_id=product.id))  # Redirecionar para a página de confirmação de cadastro
    return render_template('productaddition.html', title='Adicionar Produto', form=form)


@app.route('/product_confirmation/<int:product_id>', methods=['GET'])
def product_confirmation(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_confirmation.html', title='Confirmação de Cadastro', product=product)


# Rota para o usuario editar um produto:
@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if product.owner != current_user:
        abort(403)  # Forbidden

    form = ProductForm(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('products'))

    return render_template('edit_product.html', title='Editar Produto', form=form, product=product)