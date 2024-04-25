from flask import render_template, request
from flask import redirect
from flask import url_for
from app import app
from app import db
from app.forms import Cadastroform
from app.models import User

@app.route('/')  #  rota e renderização da página inicial
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])  #  Login do usuario
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        #  Lógica de autenticação:
        # Verifica se o usuário existe no banco de dados:
        user = User.query.filter_by(email=email).first()
        if user:
            # Se o usuário existir, verifica se a senha está correta
            if user.check_password(senha):
                print("Login bem-sucedido, redirecionando para a página do usuário")
                # Login bem-sucedido
                return redirect(url_for('page_usuario'))
            else:
                # Senha incorreta
                return render_template('login.html', error='Senha incorreta')
        else:
            # Usuário não encontrado
            return render_template('login.html', error='Usuário não encontrado')

    # Se o método HTTP for GET, renderiza apenas o template de login
    return render_template('login.html')

@app.route('/usuario')  #  Pagina do usuário
def page_usuario():
    return render_template('usuario.html')

@app.route('/usuario')  #  rota para que apenas usuários autenticados possam ter acesso a ela
def usuario():
    # Verifica se o usuário está autenticado:
    if 'usuario_id' in session:
        # Se sim, renderiza a página do usuário:
        return render_template('usuario.html')
    else:
        # Se não, redireciona para a página de login:
        return redirect(url_for('login'))

@app.route('/cadastro_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        # Capturar os dados do formulário
        name = request.form['name']
        type = request.form['type']
        corante = request.form['corante']
        transgenico = request.form['transgenico']
        aditivos = request.form['aditivos']
        ogm = request.form['ogm']

        # Cria um novo produto com os dados capturados:
        new_product = Product(
            name=name,
            type=type,
            corante=corante,
            transgênico=transgenico,
            aditivos_quimicos=aditivos,
            organismo_geneticamente_modificado=ogm
        )

        # Adiciona o novo produto ao banco de dados
        db.session.add(new_product)
        db.session.commit()

        # Redireciona para a rota da API para obter todos os produtos:
        return redirect(url_for('get_products'))

        # Se o método HTTP for GET, renderiza o formulário de cadastro de produto
    return render_template('novoproduto.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = Cadastroform()
    if form.validate_on_submit():
        # Verifica se o email já está cadastrado
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            # Se o email já estiver cadastrado, exibe uma mensagem de erro
            return render_template('cadastro.html', form=form, error='Este email já está cadastrado.')

        # Se o email não estiver cadastrado, cria um novo usuário:
        novo_usuario = User(
            nome=form.nome.data,
            email=form.email.data,
            senha_hash=form.senha_hash.data
        )
        novo_usuario.set_password(form.senha_hash.data)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('page_usuario'))

    # Se o formulário não for submetido ou não for válido, renderiza o template de cadastro:
    return render_template('cadastro.html', form=form)

