import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils import ComplexNumber

class TestComplexNumber:
    zero_torance = 1e-10
    c1 = ComplexNumber(1.2, 3.4)
    c2 = ComplexNumber(4.5, 6.7)

    def test＿ComplexNumber_add(self):
        c3 = self.c1 + self.c2
        assert abs(c3.real - (5.7)) < self.zero_torance
        assert abs(c3.imag - (10.1)) < self.zero_torance

    def test＿ComplexNumber_sub(self):
        c3 = self.c1 - self.c2
        assert abs(c3.real - (-3.3)) < self.zero_torance
        assert abs(c3.imag - (-3.3)) < self.zero_torance

    def test＿ComplexNumber_mul(self):
        c3 = self.c1 * self.c2
        assert abs(c3.real - (-17.38)) < self.zero_torance
        assert abs(c3.imag - (23.34)) < self.zero_torance


    def test＿ComplexNumber_div(self):
        c3 = self.c1 / self.c2
        assert abs(c3.real - (0.43260669327602086)) < self.zero_torance
        assert abs(c3.imag - (0.11145225667792447)) < self.zero_torance