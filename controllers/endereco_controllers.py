from models.endereco_models import Endereco
from db import db
import json
from flask import make_response, request

def create_endereco(endereco_data):
    novo_endereco = Endereco(
        endereco = Endereco(
        cep=endereco_data['cep'],
        logradouro=endereco_data['logradouro'],
        complemento=endereco_data['complemento'],
        unidade=endereco_data['unidade'],
        bairro=endereco_data['bairro'],
        localidade=endereco_data['localidade'],
        uf=endereco_data['uf'],
        estado=endereco_data['estado'],
        regiao=endereco_data['regiao'],
        ibge=endereco_data['ibge'],
        gia=endereco_data['gia'],
        ddd=endereco_data['ddd'],
        siafi=endereco_data['siafi']
    )

    )
    db.session.add(novo_endereco)
    db.session.commit()
    response = make_response(
        json.dumps({  
            'mensagem': 'Endereco cadastrado com sucesso.',  
            'carro': novo_endereco.json()  
        }, sort_keys=False)  
    )
    response.headers['content-Type'] = 'application/json'
    return response

def get_endereco():
    endereco = Endereco.query.all()

    if not endereco:
        response = make_response(
            json.dumps({
                'mensagem': 'Nenhum endereco encontrado.',
                'dados': []
            }, ensure_ascii=False, sort_keys=False)
        )
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Lista de endereços.',
                'dados': [endereco.json() for enderecos in endereco]
            }, ensure_ascii=False, sort_keys=False)
        )
    response.headers['Content-Type'] = 'application/json'  
    return response


def get_enderecos_by_id(endereco_id):
    endereco = Endereco.query.get(endereco_id)  

    if endereco: 
        response = make_response(
            json.dumps({
                'mensagem': 'Endereco encontrado.',
                'dados': endereco.json() 
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    else:
        
        response = make_response(
            json.dumps({'mensagem': 'Endereco não encontrado.', 
                        'dados': {}}, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    

def get_endereco_by_nome(endereco_nome):
    endereco = Endereco.query.filter_by(nome=endereco_nome).first() 

    if endereco:
        response = make_response(
            json.dumps({
                'mensagem': 'endereco encontrado.',
                'dados': endereco.json()
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'endereco não encontrado.',
                'dados': {}
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response, 
        404


def create_endereco(endereco_data):
   
    if not all(key in endereco_data for key in ['cep', 'logradouro', 'complemento', 'unidade','bairro', 'localidade', 'uf', 'estado', 'regiao', 'ibge', 'gia', 'ddd', 'siafi' ]):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafio são obrigatórios.'
            }, ensure_ascii=False),
            400 
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    
    novo_endereco = Endereco(
        cep=endereco_data['cep'],
        logradouro=endereco_data['logradouro'],
        complemento=endereco_data['complemento'],
        unidade=endereco_data['unidade'],
        bairro=endereco_data['bairro'],
        localidade=endereco_data['localidade'],
        uf=endereco_data['uf'],
        estado=endereco_data['estado'],
        regiao=endereco_data['regiao'],
        ibge=endereco_data['ibge'],
        gia=endereco_data['gia'],
        ddd=endereco_data['ddd'],
        siafi=endereco_data['siafi']
    )
    
    db.session.add(novo_endereco)  
    db.session.commit()  

    
    response = make_response(
        json.dumps({
            'mensagem': 'Endereco cadastrado com sucesso.',
            'endereco': novo_endereco.json() 
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json' 
    return response

def update_endereco(endereco_id, endereco_data):
    endereco = Endereco.query.get(endereco_id)  
    if not endereco:  
        response = make_response(
            json.dumps({'mensagem': 'Endereco não encontrado.'
            }, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json' 
        return response


    if not all(key in endereco_data for key in ['cep', 'logradouro', 'complemento', 'unidade','bairro', 'localidade', 'uf', 'estado', 'regiao', 'ibge', 'gia', 'ddd', 'siafi']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafio são obrigatórios são obrigatórios.'
            }, ensure_ascii=False),
            400 
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    
        endereco.cep=endereco_data['cep'],
        endereco.logradouro=endereco_data['logradouro'],
        endereco.complemento=endereco_data['complemento'],
        endereco.unidade=endereco_data['unidade'],
        endereco.bairro=endereco_data['bairro'],
        endereco.localidade=endereco_data['localidade'],
        endereco.uf=endereco_data['uf'],
        endereo.estado=endereco_data['estado'],
        endereco.regiao=endereco_data['regiao'],
        endereco.ibge=endereco_data['ibge'],
        endereco.gia=endereco_data['gia'],
        endereco.ddd=endereco_data['ddd'],
        endereco.siafi=endereco_data['siafi']

    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'endereco atualizado com sucesso.',
            'endereco': endereco.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  
    return response

def delete_endereco(endereco_id):
    confirmacao = request.args.get('confirmacao')  

    if confirmacao != 'true':  
        response = make_response(
            json.dumps({'mensagem': 'Confirmação necessária para excluir o endereco.'}, ensure_ascii=False),
            400 
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    endereco = Endereco.query.get(endereco_id) 
    if not endereco: 
        response = make_response(
            json.dumps({'mensagem':'endereco não encontrado.'}, ensure_ascii=False),
            404 
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(endereco)  
    db.session.commit()  


    response = make_response(
        json.dumps({'mensagem': 'Endereco excluído com sucesso.'}, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
