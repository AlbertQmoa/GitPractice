import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils import ComplexNumber

zero_torance = 1e-10
c1 = ComplexNumber(1.2, 3.4)
c2 = ComplexNumber(4.5, 6.7)

def test＿ComplexNumber_add():
    c3 = c1 + c2
    assert abs(c3.real - (5.7)) < zero_torance
    assert abs(c3.imag - (10.1)) < zero_torance


def test＿ComplexNumber_sub():
    c3 = c1 - c2
    assert abs(c3.real - (-3.3)) < zero_torance
    assert abs(c3.imag - (-3.3)) < zero_torance


def test＿ComplexNumber_mul():
    c3 = c1 * c2
    assert abs(c3.real - (-17.38)) < zero_torance
    assert abs(c3.imag - (23.34)) < zero_torance


def test＿ComplexNumber_div():
    c3 = c1 / c2
    assert abs(c3.real - (0.43260669327602086)) < zero_torance
    assert abs(c3.imag - (0.11145225667792447)) < zero_torance