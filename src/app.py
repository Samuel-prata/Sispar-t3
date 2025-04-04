# RESPONSAVEL POR CRIAR A APLICAÇÃO 

from flask import Flask
from src.controller.colaborador_controller import bp_colaborador

def create_app():
    app = Flask(__name__) 
    app.register_blueprint(bp_colaborador)
    return app    