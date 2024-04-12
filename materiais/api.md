# Introdução ao uso e criação de APIs

Bem-vindo(a) ao material de introdução a APIs. As APIs (Interface de Programação de Aplicativos) são conjuntos de regras e definições que permitem a comunicação entre diferentes softwares. Elas desempenham um papel fundamental na integração de sistemas e no compartilhamento de dados entre aplicativos.


## Por que as APIs são importantes no desenvolvimento de software?

- **Reutilização de Funcionalidades**: As APIs permitem que os desenvolvedores reutilizem funcionalidades existentes sem precisar reinventar a roda.
- **Integração de Sistemas**: Elas facilitam a integração de diversos sistemas, permitindo que aplicativos diferentes se comuniquem entre si.
- **Acesso a Recursos Externos**: As APIs fornecem acesso controlado a recursos externos, como dados de terceiros ou serviços web.
- **Facilidade de Desenvolvimento**: Ao utilizar APIs, os desenvolvedores podem se concentrar em desenvolver funcionalidades específicas de seus aplicativos, em vez de lidar com todos os aspectos da implementação.


### Exemplos de APIs populares e seus casos de uso

- **Google Maps API**: Permite integrar mapas e dados de localização em aplicativos web e móveis.

```python
  import requests

  def get_location(address):
      url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=SUA_API_KEY"
      response = requests.get(url)
      data = response.json()
      return data['results'][0]['geometry']['location']

  location = get_location("Centro Universitário Unisagrado, Bauru, SP")
  print(location)

```

#### Exemplos de APIs da Web:

- **RESTful APIs**: Utilizam os princípios arquiteturais REST (Representational State Transfer) para definir operações sobre recursos, utilizando métodos HTTP como GET, POST, PUT, PATCH e DELETE.
- **SOAP APIs**: Utilizam o protocolo SOAP (Simple Object Access Protocol) para troca de mensagens XML estruturadas entre sistemas.
- **GraphQL APIs**: Permitem que os clientes solicitem exatamente os dados que precisam, de forma flexível e eficiente.

### Verbos HTTP

As APIs RESTful utilizam os verbos HTTP para indicar a operação a ser realizada sobre um recurso. Os principais verbos HTTP utilizados em APIs REST são:

- **GET**: Utilizado para recuperar recursos existentes.
- **POST**: Utilizado para criar um novo recurso.
- **PUT**: Utilizado para substituir um recurso existente por completo.
- **PATCH**: Utilizado para atualizar parcialmente um recurso existente.
- **DELETE**: Utilizado para excluir um recurso existente.

### Códigos de Status HTTP

Os códigos de status HTTP são utilizados para indicar o resultado de uma requisição HTTP. Alguns dos códigos de status comuns em APIs REST incluem:

- **200 OK**: Indica que a requisição foi bem-sucedida.
- **201 Created**: Indica que o recurso foi criado com sucesso.
- **400 Bad Request**: Indica que a requisição possui um formato inválido.
- **404 Not Found**: Indica que o recurso solicitado não foi encontrado.
- **500 Internal Server Error**: Indica que ocorreu um erro interno no servidor.


### Criando uma API com Python utilizando o microframework Flask

Neste exemplo, vamos criar uma API simples utilizando o framework [Flask](https://flask.palletsprojects.com/en/3.0.x/) em Python. Flask é um framework leve e flexível que facilita a criação de aplicativos web e APIs. Ainda, além do Flask, você pode utilizar outros frameworks, como por exemplo, [FastAPI](https://fastapi.tiangolo.com/), [Django](https://www.djangoproject.com/), [Pyramid](https://trypyramid.com/), etc.


### Exemplo de código

A seguir, apresentamos um exemplo de código que demonstra como criar uma API com Flask para gerenciar livros.

Entretanto, para funcionar a sua aplicação, vamos instalar o Flask:

```bash
pip3 install Flask
```

Assim, logo após ter instalado o Flask, você poderá executar a seguinte API.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemplo de dados (poderiam vir de um banco de dados)
livros = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell"}
]

# Rota para listar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Rota para obter um livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        return jsonify(livro)
    return jsonify({"mensagem": "Livro não encontrado"}), 404

# Rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return jsonify({"mensagem": "Livro adicionado com sucesso"}), 201

# Rota para atualizar um livro existente
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro_atualizado = request.json
    for livro in livros:
        if livro['id'] == id:
            livro.update(livro_atualizado)
            return jsonify({"mensagem": "Livro atualizado com sucesso"})
    return jsonify({"mensagem": "Livro não encontrado"}), 404

# Rota para excluir um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    global livros
    livros = [livro for livro in livros if livro['id'] != id]
    return jsonify({"mensagem": "Livro excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
```

Você pode executar com o seguinte comando:

```bash
python3 run.py
```

## Autenticação e Autorização em APIs

A autenticação e a autorização são dois aspectos fundamentais da segurança em APIs, garantindo que apenas usuários autorizados tenham acesso aos recursos e funcionalidades disponibilizados pela API.

### Autenticação

A autenticação é o processo de verificar a identidade de um usuário ou aplicativo que está tentando acessar a API. Ela garante que apenas usuários legítimos tenham permissão para utilizar os recursos da API. Existem várias estratégias de autenticação comuns em APIs:

- **Chaves de API**: Cada usuário ou aplicativo recebe uma chave de API exclusiva que deve ser incluída em cada requisição. Isso permite que o servidor da API identifique e autentique o solicitante.
- **Token de Acesso**: Após a autenticação bem-sucedida, o servidor da API gera um token de acesso temporário que deve ser incluído em requisições subsequentes. Os tokens de acesso são frequentemente utilizados em APIs RESTful com OAuth.
- **Autenticação Baseada em Token**: Os tokens de acesso são armazenados de forma segura e associados a uma sessão de usuário. Eles são frequentemente utilizados em combinação com cookies ou cabeçalhos de autorização.
- **OAuth (Open Authorization)**: Um protocolo de autorização que permite que os usuários concedam acesso a recursos protegidos a terceiros sem compartilhar suas credenciais diretamente. O OAuth é amplamente utilizado em APIs de terceiros, como as APIs do Google e do Facebook.

### Autorização

A autorização determina quais recursos e funcionalidades um usuário autenticado tem permissão para acessar. Ela garante que os usuários tenham acesso apenas aos recursos que são relevantes para suas necessidades e permissões. Alguns conceitos importantes relacionados à autorização incluem:

- **Permissões**: As permissões definem as ações específicas que um usuário está autorizado a realizar em um recurso. Por exemplo, um usuário pode ter permissão para visualizar um recurso, mas não para modificá-lo.
- **Papéis (Roles)**: Os papéis agrupam conjuntos de permissões relacionadas. Por exemplo, um usuário pode ser atribuído ao papel de "administrador", concedendo acesso total a todos os recursos e funcionalidades da API, enquanto outro usuário pode ser atribuído ao papel de "usuário comum", com acesso limitado a recursos específicos.
- **Políticas de Acesso**: As políticas de acesso definem as regras que determinam quais usuários têm permissão para acessar quais recursos. Elas geralmente são baseadas em papéis, permissões e outros atributos do usuário.

Ao desenvolver uma API, é fundamental implementar medidas adequadas de autenticação e autorização para proteger os recursos e garantir a segurança dos usuários e dados. Isso envolve a escolha de estratégias de autenticação apropriadas, a definição de permissões e papéis de forma granular e a implementação de políticas de acesso robustas.

Além disso, abaixo há um código Python de exemplo integrando com o [Google Firebase](https://firebase.google.com/?hl=pt) para autenticação.

```python
from flask import Flask, request, jsonify
from firebase_admin import auth
from firebase_admin import credentials
from dotenv import load_dotenv
import firebase_admin
import json
import requests
import os

cred = credentials.Certificate("auth-firebase.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__)
load_dotenv()

# Método para verificação dos tokens recebidos via requisição
def verify_token():
    id_token = request.headers.get('Authorization')
    if not id_token:
        return jsonify({'error': 'Token não fornecido'}), 401

    try:
        decoded_token = auth.verify_id_token(id_token)
        request.uid = decoded_token['uid']
    except auth.InvalidIdTokenError:
        return jsonify({'error': 'Token inválido'}), 401
    except auth.ExpiredIdTokenError:
        return jsonify({'error': 'Token expirado'}), 401

# Método com o decorator do Flask para executar antes do request
@app.before_request
def before_request_func():
    if request.endpoint not in ['login', 'signup']:
        return verify_token()

# Método para cadastrar novos usuários no Firebase para autenticação
@app.route('/signup', methods=['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']

    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print(user.uid)
        return jsonify({'message': 'User created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Método para realizar login no Google Firebase recebendo token
@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={os.getenv('FIREBASE_API_KEY')}"

    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        return jsonify({'error': 'Credenciais inválidas'}), 401
    json_response = json.loads(response.text)
    return jsonify({
        'message': 'Login realizado com sucesso',
        'token': json_response['idToken'],
        'refreshToken': json_response['refreshToken']
    }), 200

# Método de teste para verificar acesso por meio de um token
@app.route('/endpoint_protegido', methods=['POST'])
def endpoint_protegido():
    return jsonify({'message': 'Acessando endpoint protegido'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```