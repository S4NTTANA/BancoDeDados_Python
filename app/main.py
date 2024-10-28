from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session

import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuário.
    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usuário cadastrados.
    print("\nListando usuarios cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario.nome} - \nEmail: {usuario.email} - \nSenha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main()