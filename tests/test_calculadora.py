# tests/test_calculadora.py

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculadora import Calculadora


def test_sumar():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5, "La suma de 2 + 3 debe ser 5"
