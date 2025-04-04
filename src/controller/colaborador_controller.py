
from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db

# request -> trabalha com as requisições. Pega o conteúdo da requisição
# jsonify -> Trabalha com as respostas. Converte um dado em Json

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

dados = [
        {'id': 1,'nome': 'Karynne Moreira', 'cargo': 'CEO', 'cracha': '010101'},
        {'id': 2,'nome': 'Samuel Silverio', 'cargo': 'CTO', 'cracha': '74512'},
        {'id': 3,'nome': 'Thales Reis', 'cargo': 'Desenvolvedor Back-end Java', 'cracha': '14523'},
        {'id': 4,'nome': 'Eduardo Gomes', 'cargo': 'DevOps', 'cracha': '78412'},
        {'id': 5,'nome': 'Gabriel Silvano', 'cargo': 'Desenvolvedor Front-end React', 'cracha': '96523'},
        {'id': 6,'nome': 'Suelen Braga', 'cargo': 'Infra', 'cracha': '251473'}
    ]

@bp_colaborador.route('/pegar-dados')
def pegar_dados():
    return dados

@bp_colaborador.route('/cadastrar', methods=['POST'])
def cadastrar_novo_colaborador(): 
    
    dados_requisicao = request.get_json() 
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'], # Pegue do json o valor relacionado a chave nome
        email=dados_requisicao['email'],
        senha=dados_requisicao['senha'],
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
#   INSERT INTO tb_colaborador (nome, email, senha, cargo, salario) VALUES (VALOR1,VALOR2,VALOR3,VALOR4,VALOR5)
    db.session.add(novo_colaborador)
    db.session.commit() # Essa linha executa a query
    
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'} ), 201

# Endereco/colaborador/atualizar/1
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_do_colaborador(id_colaborador):
    
    dados_requisicao = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break 
    
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']

    return jsonify({'mensagem': 'Dados do colaborador atualizados com sucesso'}), 200