from flask import Flask

app = Flask(__name__)

#Criação de um aplicativo Flask - Cadastro de usuario

# Dados fictícios para simular um banco de dados de usuários
db_usuarios = [
    {"id": 1, "name": "Maria", "email": "maria1@maria.com.br"},
    {"id": 2, "name": "Pedro", "email": "jose2@jose.com.br"},
    # ...
]

@app.route('/cadastrar', methods = ['POST'])
def cadastrar():
    return 'Cadastro realizado com sucesso'

@app.route('/usuarios', methods=['GET'])
def mostrar_usuarios():
    return db_usuarios

@app.route('/atualizar', methods = ['PUT'])
def atualizar():
    return 'Atualizado com sucesso'

@app.route('/excluir', methods=['DELETE'])
def excluir():
    return 'Usuário excluído'



app.run(debug=True)


