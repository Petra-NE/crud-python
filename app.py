from flask_restx import Api, Resource, fields
from flask import Flask

from db import db_usuarios

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='API de Cadastro de Usuários',
    description='API para cadastrar e gerenciar usuários',
)

ns = api.namespace('User', description='CRUD de Cadastro de Usuário')
modelo = api.model('User', {
    'id': fields.Integer, 
    'name': fields.String,
    'address': fields.String
})

@ns.route('/usuarios', methods=['GET'])
class mostrar_usuarios(Resource):
    def get(self):
        '''Listar todos os usuários'''
        return db_usuarios

#Criação de um aplicativo Flask - Cadastro de usuario
@ns.route('/cadastrar', methods = ['POST'])
class cadastrar(Resource):
    def post(self):
        '''Cria um novo usuário'''
        return 'Cadastro realizado com sucesso'

@ns.route('/atualizar', methods = ['PUT'])
class atualizar(Resource):
    def put(self):
        '''Atualiza usuário existente'''
        return 'Atualizado com sucesso'

@ns.route('/excluir', methods=['DELETE'])
class excluir(Resource):
    def delete():
        '''Excluir usuário'''
        return 'Usuário excluído'



app.run(debug=True)


