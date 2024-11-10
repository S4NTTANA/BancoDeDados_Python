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

    def pesquisar_usuario_por_id(self):
        try:
            id = input("Informe o id do usuário que deseja procurar: ")
            checando_usuario = self.repository.pesquisar_usuario_por_id(id=id)

            if checando_usuario:
                print(f"Nome: {checando_usuario.nome}")
                print(f"Email: {checando_usuario.email}")
                print(f"Senha: {checando_usuario.senha}")
            else:
                print("Usuário não encontrado.")
        except TypeError as erro:
            print(f"Usuário não encontrado.")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
    
    def atualizar_usuario(self):

        try:
            id = int(input("\nInforme o id do usuário que deseja atualizar: "))
            usuario_modidicado = self.repository.pesquisar_usuario_por_id(id = id)

            if usuario_modidicado:
                    usuario_modidicado.nome = input("Digite o nome do aluno que será atualizado: ")
                    usuario_modidicado.email = input("Digite o e-mail do aluno que será atualizado: ")
                    usuario_modidicado.senha = input("Digite o senha do aluno que será atualizado: ")
                    self.repository.salvar_usuario(usuario_modidicado)
            else:
                print("Usuário não encontrado!") 
            
        except TypeError as erro:
            print("erro ao deletar ususario")
        except Exception as erro:
            print (f"Ocorreu um erro inesperado: {erro}")

    def excluir_usuario(self):
        try:
            id = input("Informe o id do usuário: ")
            excluir_cliente = self.repository.pesquisar_usuario_por_id(id)

            if excluir_cliente:
                self.repository.excluir_usuario(excluir_cliente)
                print("Usuário excluido com sucesso.")
            else:
                print("Erro ao excluir Usuário")
        
        except TypeError as erro:
            print(f"Erro ao excluir usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")