from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session
from models.usuario_model import Usuario

import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        
         print("1 - Adcionar usuário")
         print("2 - Pesquisar um usuario")
         print("3 - Atualizar dados de um usuário")
         print("4 - Excluir um usuário")
         print("5 - Exibir todos os usuarios cadastrados") 
         print("0 - Sair")

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
                try:
                    id = int(input("\nInforme o id do usuário que deseja procurar: "))
                    usuario = repository.session.query(Usuario).filter_by(id = id).first()
                    if usuario:
                        print(f"\nID: {usuario.id} \nNome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha}")
                    return
                except TypeError as erro:
                    print("erro ao deletar ususario")

            case 3:
                    print ("Atualizando dados do aluno.")
                    service.atualizar_usuario(Usuario)
            case 4:
                repository.excluir_usuario(usuario)
                session.delete(usuario)
                session.commit()
                session.refresh(usuario)
                break
                
            case 5:
                # Listar todos os usuário cadastrados.
                print("\nListando usuarios cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"\nNome: {usuario.nome} - \nEmail: {usuario.email} - \nSenha: {usuario.senha}")
                
          
                 
            



if __name__ == "__main__":
    os.system("cls || clear")
    main()