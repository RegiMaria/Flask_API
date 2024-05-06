Atualização 4 - 06/05/2024

**Templates**

- register.html:
Atualizamos o registro de usuário (/register);

- login.html
Atulaizamos o login do usuárion(/login);


**Routes**

register e login

Atualizmos a validação dos formulários. Anteriormente estávamos utilizando o objeto **request** 
do Flask para acessar os dados do formulário diretamente. Agora estamos utilizando as **classes de formulário (RegustrationForm e LoginForm)** e **Flask-WTF** para criar e validar os dados do formulário. Por último, estamos utilizando a função **login_user** e a extensão**Bcrypt** para armazenar as senhas de forma segura.

**Sintaxe entre chaves percentuais {% %}**
Utilizamos {% if current_user.is_authenticated %}, uma estrutura condicional que verifica se o usuário atual está autenticado, para exibir ou ocultar conteúdo com base no estado de autenticação do usuário.

**Uso de @login_required**

Decorador fornecido pelo **Flask_login** (extensão do flask).
Para controle de acesso a rotas específicas. Rotas que só poderam ser acessadas se o usuário
estiver logado.

**Novas funções para configurar o LoginManager** (do flask_login)

1. login_manager.login_view='login':

Configura a página para a qual os usuários serão redirecionados quando tentarem acessar uma página restrita sem estar autenticados.

2. login_manager.login_message= 'Por favor, realize o login': 

Esta linha define a mensagem que será exibida aos usuários quando forem redirecionados para a página de login.

3. login_manager.login_message_category='info': 

Esta linha define a categoria da mensagem que será exibida aos usuários ao redirecioná-los para a página de login.

**Font Awsome:**

Adicionamos o ícone fas fas-paw;
