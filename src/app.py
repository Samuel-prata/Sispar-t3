# RESPONSAVEL POR CRIAR A APLICAÇÃO 
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec", # <-- Da um nome de referencia para a documentacao
            "route": "/apispec.json/", # <- Rota do arquivo JSON para a construção da documentação
            "rule_filter": lambda rule: True, # <-- Todas as rotas/endpoints serão documentados
            "model_filter": lambda tag: True, # <-- Especificar quuais modelos da entidade serão documentados
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

def create_app():
    app = Flask(__name__) # <-- instancia do Flask
    CORS(app, origins="*") # <---- A politica de CORS seja implementada em TODA A APLICAÇÃO 
    app.register_blueprint(bp_colaborador)
    app.config.from_object(Config)
    
    db.init_app(app) # Inicia a conexão com o banco de dados
    
    Swagger(app, config=swagger_config)
    
    with app.app_context(): # Se as tabelas não existem, crie.
        db.create_all()
    return app    