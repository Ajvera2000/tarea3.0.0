import pytest
from app.main import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 3) == 2

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(5, 0)