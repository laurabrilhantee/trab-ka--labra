from flask import Blueprint, request  
from controllers.endereco_controllers import create_endereco, update_endereco, delete_endereco, get_endereco

endereco_routes = Blueprint('endereco_routes', __name__)  

@endereco_routes.route('/Endereco', methods=['GET'])
def endereco_get():
    return get_endereco()

# Rota para criar um novo funcionário (POST)
@endereco_routes.route('/Endereco', methods=['POST'])
def endereco_post():
    return create_endereco(request.json)

# Rota para atualizar um funcionário pelo ID (PUT)
@endereco_routes.route('/Enderecdo/<int:endereco_id>', methods=['PUT'])
def endereco_put(endereco_id):
    return update_endereco(endereco_id, request.json)

# Rota para excluir um funcionário pelo ID (DELETE)
@endereco_routes.route('/Endereco/<int:funcionario_id>', methods=['DELETE'])
def endereco_delete(endereco_id):
    return delete_endereco(endereco_id)
