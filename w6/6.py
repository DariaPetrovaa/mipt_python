from math import sqrt, atan, sin, cos

class Complex:
    
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        a1 = self.real + other.real
        a2 = self.imaginary + other.imaginary
        return Complex(a1, a2)

    def __sub__(self, other):
        a1 = self.real - other.real
        a2 = self.imaginary - other.imaginary
        return Complex(a1, a2)

    def __truediv__(self, other):
        a1 = other.real**2 + other.imaginary**2
        a2 = self.real*other.real + self.imaginary*other.imaginary
        a3 = self.imaginary*other.real - self.real*other.imaginary
        ans1 = a2/a1
        ans2 = a3/a1
        return Complex(ans1, ans2)

    def __mul__(self, other):
        a1 = self.real*other.real - self.imaginary*other.imaginary
        a2 = self.imaginary*other.real + self.real*other.imaginary
        return Complex(a1, a2)

    def __pow__(self,other):
        r = sqrt(self.real**2 + self.imaginary**2)
        angle = atan (self.imaginary/self.real)
        ans1 = cos(other*angle)
        ans2 = sin(other*angle)
        a1 = (r**other)*ans1
        a2 = (r**other)*ans2
        return Complex(a1, a2)

    def __neg__(self):
        return Complex(self.real, -self.imaginary)

    def __abs__(self):
        r = sqrt(self.real**2 + self.imaginary**2)
        return r

A = Complex(2,5)
B = Complex (3,7)
C = A + B
print(C.real, C.imaginary)
C = A - B
print(C.real, C.imaginary)
C= A * B
print(C.real, C.imaginary)
C = A/B
print(C.real, C.imaginary)
C = A**5
print(C.real, C.imaginary)
C = -A
print(C.real, C.imaginary)
C = abs(A)
print (C)
