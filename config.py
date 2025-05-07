# Armazenar as configurações do ambiente de desenvolvimento
from os import environ # Esse arquivo tem acesso as varíaveis de ambiente
from dotenv import load_dotenv # Carregamento das variáveis de ambiente nesse arquivo

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD') # Puxa a variável e utiliza para a conexão
    SQLALCHEMY_TRACK_MODIFICATIONS=False # OTIMIZA as querys no banco de dados
    