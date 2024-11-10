from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    # Definindo características da classe
    def __init__(self, nome:str, email:str, senha:str):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser um texto !")
        if not isinstance(email, str):
            raise TypeError("O email deve ser um texto !")
        if not isinstance(senha, str):
            raise TypeError("A senha deve ser um texto !")
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)