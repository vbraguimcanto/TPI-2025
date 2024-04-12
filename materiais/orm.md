# Introdução ao ORM em Python

O Mapeamento Objeto-Relacional (ORM) é uma técnica fundamental no desenvolvimento de software, especialmente em aplicações que utilizam bancos de dados relacionais. Em Python, o ORM permite que os desenvolvedores trabalhem com objetos em código Python, enquanto o ORM se encarrega de traduzir esses objetos para estruturas de banco de dados relacionais, como tabelas, colunas e relacionamentos.

## Por que usar ORM?

O uso de ORM traz uma série de benefícios para o desenvolvimento de software:

- **Abstração do Banco de Dados**: Os desenvolvedores podem trabalhar com objetos familiares em vez de lidar diretamente com consultas SQL, o que simplifica o código e torna-o mais legível.
  
- **Produtividade**: ORM automatiza muitas tarefas relacionadas ao acesso e manipulação de dados, permitindo que os desenvolvedores se concentrem mais na lógica de negócios de suas aplicações.

- **Portabilidade**: ORM geralmente oferece suporte a vários bancos de dados, facilitando a migração entre diferentes sistemas de banco de dados sem alterações significativas no código.

## Principais Bibliotecas ORM em Python

Existem várias bibliotecas ORM populares em Python, cada uma com suas próprias características e vantagens:

- **SQLAlchemy**: Uma biblioteca ORM poderosa e altamente configurável, amplamente utilizada em projetos Python de grande escala.
  
- **Django ORM**: Integrado ao framework Django, oferece uma interface simples e direta para interagir com o banco de dados em projetos Django.

- **Peewee**: Uma biblioteca ORM leve e fácil de aprender, ideal para projetos menores ou para aqueles que preferem uma abordagem mais simples.

No restante deste material, exploraremos os conceitos fundamentais do ORM em Python, mostrando como criar modelos de dados, realizar operações CRUD, executar consultas e abordar considerações importantes, como segurança, desempenho e integração com frameworks web.


## Exemplo de Uso do SQLAlchemy em Python

Neste exemplo, vamos utilizar o SQLAlchemy para criar um modelo de dados para uma aplicação de gerenciamento de usuários simples. Vamos definir uma entidade `User` com os campos `id`, `username` e `email`.

### Instalando o SQLAlchemy

Antes de começarmos, certifique-se de ter o SQLAlchemy instalado. Você pode instalá-lo via pip:

```bash
pip install SQLAlchemy
```

### Definindo o Modelo de Dados

No código abaixo há um exemplo de como definir o modelo de dados que será criado.


```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Cria uma instância do SQLAlchemy Engine usando o SQLite
engine = create_engine('sqlite:///users.db', echo=True)

# Cria uma classe de modelo de base
Base = declarative_base()

# Define a classe de modelo de dados User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
```

### Criando as tabelas no banco de dados

Você poderá incluir o seguinte comando no seu código Python para criar as tabelas no DB.

```python
Base.metadata.create_all(engine)
```


### Inserindo dados no banco de dados

O código abaixo fornece um exemplo de como criar um usuário no banco de dados.

```python
from sqlalchemy.orm import sessionmaker

# Cria uma sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Cria um novo usuário
new_user = User(username='victor', email='victor@victor.com')

# Adiciona o usuário à sessão
session.add(new_user)

# Commit para salvar no banco de dados
session.commit()

# Fecha a sessão
session.close()
```

### Consultando dados no banco de dados


O código abaixo fornece um exemplo de como consultar dados no banco de dados.

```python
# Abre uma nova sessão
session = Session()

# Consulta todos os usuários
users = session.query(User).all()

# Imprime os resultados
for user in users:
    print(user)

# Fecha a sessão
session.close()
```

### Exemplo de API com o uso de banco de dados


O código abaixo mostra uma API desenvolvida em Flask com o uso de banco de dados para persistência.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Criação do Modelo da Tabela: User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all,delete')

# Criação do Modelo da Tabela: Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Endpoint para a criação de um usuário
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Endpoint para a criação de um post
@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()
    user = User.query.get(data['user_id'])
    if user:
        new_post = Post(title=data['title'], content=data['content'], author=user)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created successfully"}), 201
    else:
        return jsonify({"message": "User not found"}), 404

# Endpoint para deletar um usuário
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Endpoint para buscar usuários
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "posts": [{"id": post.id, "title": post.title, "content": post.content} for post in user.posts]
        }
        user_list.append(user_data)
    return jsonify(user_list), 200

if __name__ == '__main__':
    # Instrução para a criação das tabelas no banco de dados
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
