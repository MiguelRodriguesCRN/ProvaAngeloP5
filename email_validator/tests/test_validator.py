import pytest
from email_validator.validator import EmailValidator

validator = EmailValidator()

def test_email_valido():
    assert validator.is_valid("usuario@dominio.com")

def test_email_sem_arroba():
    assert not validator.is_valid("usuariodominio.com")

def test_email_sem_ponto():
    assert not validator.is_valid("usuario@dominio")

def test_email_com_espaco():
    assert not validator.is_valid("usuario @dominio.com")

def test_email_com_inicio_invalido():
    assert not validator.is_valid(".usuario@dominio.com")

def test_email_com_fim_invalido():
    assert not validator.is_valid("usuario@dominio.com.")

def test_email_muito_curto():
    assert not validator.is_valid("a@b.c")

def test_email_muito_longo():
    long_email = "a" * 250 + "@gmail.com"
    assert not validator.is_valid(long_email)

def test_email_valido_com_pontos():
    assert validator.is_valid("meu.email-teste@empresa.co")
