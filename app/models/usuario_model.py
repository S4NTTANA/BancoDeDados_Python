from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from config.database import db

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

# Função para reordenar IDs
def reordenar_ids():
    # Criando uma sessão
    Session = sessionmaker(bind=db)
    session = Session()

    try:
        # Obtendo todos os usuários ordenados pelo ID
        usuarios = session.query(Usuario).order_by(Usuario.id).all()

        # Atualizando os IDs
        for novo_id, usuario in enumerate(usuarios, start=1):
            usuario.id = novo_id  # Atribui o novo ID
            session.add(usuario)  # Adiciona o objeto atualizado à sessão
            session.commit()
            session.refresh(usuario)

        # Confirma as alterações no banco de dados
    
    except Exception as e:
        session.rollback()  # Reverte em caso de erro
        print(f"Ocorreu um erro: {e}")
    
    finally:
        session.close()  # Fecha a sessão

# Se desejar, você pode chamar a função reordenar_ids() aqui ou em outro lugar em seu código.
# reordenar_ids()