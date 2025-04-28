import pytest # Traz a biblioteca de testes
import time # Manipular tempo
from src.model.colaborador_model import Colaborador
from src.app import create_app

#-------------------------CONFIGURAÇÕES PARA O TESTE--------------------------------

@pytest.fixture # Identificar funções de configurações para o teste
def app():
    app = create_app()
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()

#------------------------------------------------------------------------------------


def test_desempenho_requiscao_get(client):
    
    comeco = time.time() # Pegar a hora atual e transformar em segundos 100
    
    for _ in range(1000):
        resposta = client.get('/colaborador/todos-colaboradores')
    
    fim = time.time() - comeco
     
    assert fim < 0.2