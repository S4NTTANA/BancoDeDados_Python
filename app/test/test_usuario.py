import sys
import pytest
from app.models.usuario_model import Usuario
from app.config.database import db

@pytest.fixture
def usuario_valido():
    usuario = Usuario("Marta", "marta@gmail.com", "12345")
    return usuario

def test_valida_nome(usuario_valido):
    assert usuario_valido.nome == "Marta"

def test_valida_email(usuario_valido):
    assert usuario_valido.email == "marta@gmail.com"

def test_valida_senha(usuario_valido):
    assert usuario_valido.senha == "12345"

def test_invalida_nome():
    with pytest.raises(TypeError, match="O nome deve ser um texto !"):
        Usuario(999, "marta@gmail.com", "12345")

def test_invalida_email():
    with pytest.raises(TypeError, match="O email deve ser um texto !"):
        Usuario("Marta", 12345, "12345")

def test_invalida_senha():
    with pytest.raises(TypeError, match="A senha deve ser um texto !"):
        Usuario("Marta", "marta@gmail.com", 12345)