# Django-Catalogo-de-Filmes
Repositório para entrega de atividade de Catálogo PW3 - Desenvolvido por David Ramos e Xikkaya Martin

Este projeto consiste em um site para cadastrar e visualizar filmes.

Para utiliza-lo é necessário acessar a pasta do projeto em um prompt de comando e em seguida rodar os seguintes comando em ordem:

python -m venv venv
venv\Scripts\activate
pip install django
python manage.py createsuperuser (adicione um nome de usuário e uma senha para utilizar a página admin)
python manage.py runserver

Após estes passos é possível visualizar os filmes cadastrados pela url http://127.0.0.1:8000/

Para cadastrar novos filmes, acesse http://127.0.0.1:8000/admin/ informando o usuário e a senha informados anteriormente, clique em "Add" na parte de Filmes para ser redirecionado para a página de cadastro e em seguida passe as informações referemte ao filme e clique em "SAVE"
