import pytest
from app.models.usuario_model import Usuario
from app.config.database import db
import os 

os.system("cls||clear")

import pytest
from app.models.usuario_model import Usuario

def test_usuario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("", "maria123@gmail.com", "12345")

def test_usuario_nome_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "maria123@gmail.com", "12345") 

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("maria", "", "12345")

def test_usuario_email_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("maria", 000, "12345")  

def test_usuario_senha_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("maria", "maria123@gmail.com", "")

def test_usuario_senha_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("maria", "maria123@gmail.com", 12345)  