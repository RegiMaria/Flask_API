from flask import render_template, request,session,  redirect, url_for
from flask import redirect
from flask import url_for
from app import app
from app import db
from app.forms import Cadastroform
from app.models import Product, User
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verifica se o usuário existe no banco de dados
        user = User.query.filter_by(email=email).first()
        print("User found:", user)  # Adiciona esta linha para verificar se o usuário foi encontrado

        if user:
            # Se o usuário existir, verifica se a senha está correta
            if user.check_password(senha):
                # Login bem-sucedido
                login_user(user)
                print("Login successful")  # Adiciona esta linha para verificar se o login foi bem-sucedido
                return redirect(url_for('page_usuario'))
            else:
                # Senha incorreta
                print("Incorrect password")  # Adiciona esta linha para verificar se a senha está correta
                return render_template('login.html', error='Senha incorreta')
        else:
            # Usuário não encontrado
            print("User not found")  # Adiciona esta linha para verificar se o usuário foi encontrado
            return render_template('login.html', error='Usuário não encontrado')

    # Se o método HTTP for GET, renderiza apenas o template de login
    return render_template('login.html')

  
    
@app.route('/usuario')
def page_usuario():
    # Verifica se o usuário está autenticado
    print("User authenticated:", current_user.is_authenticated)
    if current_user.is_authenticated:
        # Se sim, renderiza a página do usuário
        return render_template('usuario.html')
    else:
        # Se não, redireciona para a página de login
        print("Redirecting to login page")
        return redirect(url_for('login'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = Cadastroform()
    if form.validate_on_submit():
        # Verifica se o email já está cadastrado
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            # Se o email já estiver cadastrado, exibe uma mensagem de erro
            return render_template('cadastro.html', form=form, error='Este email já está cadastrado.')

        # Se o email não estiver cadastrado, cria um novo usuário
        novo_usuario = User(nome=form.nome.data, email=form.email.data)
        novo_usuario.set_password(form.senha_hash.data)
        
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect (url_for('page_usuario'))
    if form.errors != {}:
        for err in form.errors.values():
            print(f'erro ao cadastrar usuário {err}')
    return render_template('cadastro.html', form=form)

        # Faz login do novo usuário
        #login_user(novo_usuario)

      

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))