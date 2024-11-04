from models.usuario_model import Usuario
from repositories.usuario_repositories import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try: 
            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)
            
            if novo_usuario:
                print("Usuario já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
    
    def atualizar_usuario(self, usuario: Usuario):

        try:
            id = int(input("\nInforme o id do usuário que deseja procurar: "))
            usuario = self.repository.session.query(Usuario).filter_by(id = id).first()

            if usuario:
                    usuario.nome = input("Digite o e-mail do aluno que será atualizado: ")
                    usuario.email = input("Digite o e-mail do aluno que será atualizado: ")
                    usuario.senha = input("Digite o e-mail do aluno que será atualizado: ")
                    self.repository.atualizar_usuario(usuario)
            else:
                print("Usuário não encontrado!") 
            
        except TypeError as erro:
            print("erro ao deletar ususario")

        self.session.commit(usuario)
        self.session.refresh(usuario)
