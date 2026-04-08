# Projeto Django - Times de Futebol

Aplicação web desenvolvida com Django para cadastro e visualização de times de futebol.

## Descrição

Este projeto permite o cadastro de times por meio da interface administrativa do Django e a visualização dessas informações em uma página web.

## Funcionalidades

- Cadastro de times via painel administrativo
- Listagem de times na página inicial
- Exibição de informações como nome, cidade e ano de fundação

## Tecnologias utilizadas

- Python
- Django

## Estrutura do projeto

```
django/
├── campeonato/
├── times/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── times/
│           └── lista_times.html
├── manage.py
└── requirements.txt
```

## Como executar o projeto

1. Clone o repositório:
```
git clone https://github.com/geovanelvs/django.git
```

2. Acesse a pasta do projeto:
```
cd django
```

3. Crie e ative o ambiente virtual:
```
python -m venv venv
venv\Scripts\activate
```

4. Instale as dependências:
```
pip install -r requirements.txt
```

5. Execute as migrações:
```
python manage.py migrate
```

6. Inicie o servidor:
```
python manage.py runserver
```

7. Acesse no navegador:
```
http://127.0.0.1:8000/
```

## Painel administrativo

Para acessar o painel administrativo:

```
http://127.0.0.1:8000/admin/
```

É necessário criar um superusuário com:

```
python manage.py createsuperuser
```

## Autor

Geovane Alves
