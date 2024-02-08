class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        divisor = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / divisor
        imag = (self.imag * other.real - self.real * other.imag) / divisor
        return ComplexNumber(real, imag)