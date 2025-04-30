# RESPONSAVEL POR CRIAR A APLICAÇÃO 
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__) # <-- instancia do Flask
    CORS(app, origins="*") # <---- A politica de CORS seja implementada em TODA A APLICAÇÃO 
    app.register_blueprint(bp_colaborador)
    app.config.from_object(Config)
    
    db.init_app(app) # Inicia a conexão com o banco de dados
    
    with app.app_context(): # Se as tabelas não existem, crie.
        db.create_all()
    
    return app    