# tests/test_calculadora.py

import pytest
from src.calculadora import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5, "La suma de 2 + 3 debe ser 5"
