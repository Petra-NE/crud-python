from flask import Flask
from db import db_usuarios

app = Flask(__name__)

#Criação de um aplicativo Flask - Cadastro de usuario


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


