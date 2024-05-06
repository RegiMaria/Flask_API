Atualização 3 - 06/05/2024

**Templates**

- register.html:
Atualizamos o registro de usuário (/register);

- login.html
Atulaizamos o login do usuárion(/login);


**Routes**

register e login

Atualizmos a validação dos formulários. Anteriormente estávamos utilizando o objeto **request** 
do Flask para acessar os dados do formulário diretamente. Agora estamos utilizando as **classes de formulário (RegustrationForm e LoginForm)** e **Flask-WTF** para criar e validar os dados do formulário. Por último, estamos utilizando a função **login_user** e a extensão**Bcrypt** para armazenar as senhas de forma segura.