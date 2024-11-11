import os
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from app.config.database import Session
from app.models.usuario_model import Usuario, reordenar_ids


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)


    while True:
        reordenar_ids()
        print ("\n===== Tabelha de Opções =====")
        print("""    1 - Adcionar usuário
    2 - Pesquisar um usuario
    3 - Atualizar dados de um usuário
    4 - Excluir um usuário
    5 - Exibir todos os usuarios cadastrados 
    0 - Sair""")

        opcao = int(input("\nInforme a opção desejada: "))

        match (opcao):
            case 1:
                # Solicitando dados para o usuário.
                print("\nAdicionando usuário.")
                nome = input("Digite seu nome: ")
                email = input("Digite seu e-mail: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)

            case 2:
                print("\n=== Pesquisando usuário por id ===")
                service.pesquisar_usuario_por_id()
                
            case 3:
                print ("Atualizando dados do usuário.")
                service.atualizar_usuario()
            case 4:
                service.excluir_usuario()
                
            case 5:
                # Listar todos os usuário cadastrados.
                print("\nListando usuarios cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"\n  Usuario {usuario.id}  \nNome: {usuario.nome}  \nEmail: {usuario.email}  \nSenha: {usuario.senha}")

            case 0:
                 print("Saindo do banco de dados.")
                 break    
             
            case _:
                 print("Opção inválida")
          
                 
if __name__ == "__main__":
    os.system("cls || clear")
    main()