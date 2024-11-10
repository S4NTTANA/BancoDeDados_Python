from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(email = email).first()
    
    def pesquisar_usuario_por_id(self, id: int):
        return self.session.query(Usuario).filter_by(id = id).first()
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def listar_usuarios(self):
        return self.session.query(Usuario).all()
    