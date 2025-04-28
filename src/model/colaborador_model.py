from src.model import db #traz a instancia do SQLALchemy para este arquivo
from sqlalchemy.schema import Column # Traz o recurso para o ORM entender que o atributo será uma coluna na tabela
from sqlalchemy.types import String, DECIMAL, Integer # Importando os tipos de dados que as colunas vão aceitar


class Colaborador(db.Model):
    
#------------------------------ATRIBUTOS-----------------------------
#   id INT AUTO_INCREMENT PRIMARY KEY
    id = Column(Integer, primary_key=True, autoincrement=True)
#   nome VARCHAR(100)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(50))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))
#---------------------------------------------------------------------
    def __init__(self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
# ----------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha
        }
        
    def all_data(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario,
            'email': self.email
        }