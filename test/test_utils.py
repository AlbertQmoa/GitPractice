import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils import ComplexNumber


def test＿ComplexNumber_add():
    c1 = ComplexNumber(1.2, 3.4)
    c2 = ComplexNumber(4.5, 6.7)
    c3 = c1 + c2
    assert c3.real == 5.7
    assert c3.imag == 10.1