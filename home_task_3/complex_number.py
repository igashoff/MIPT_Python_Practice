import sys


class ComplexNumber(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __div__(self, other):
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) /
            (other.real ** 2 + other.imaginary ** 2),
            (self.imaginary * other.real - self.real * other.imaginary) /
            (other.real ** 2 + other.imaginary ** 2)
        )

    def __str__(self):
        if (self.real != 0 and self.imaginary != 0):
            return "%.2f" % (self.real) + \
                   ' + ' if self.imaginary > 0 else ' - ' \
                   + "%.2f" % (abs(self.imaginary)) + 'i'
        elif (self.real == 0):
            return "%.2f" % (self.imaginary) + 'i'
        elif (self.imaginary == 0):
            return "%.2f" % (self.real)
        else:
            return ''


print ComplexNumber(real=1.0, imaginary=0.0)
print ComplexNumber(real=0.0, imaginary=1.0)
print ComplexNumber(real=1.0, imaginary=1.0)
print ComplexNumber(real=2.0, imaginary=-2.0)
print ComplexNumber(real=1.0, imaginary=1.0) + ComplexNumber(real=2.0, imaginary=2.0)
print ComplexNumber(real=1.0, imaginary=1.0) + ComplexNumber(real=-1.0, imaginary=-1.0)
print ComplexNumber(real=1.0, imaginary=1.0) - ComplexNumber(real=1.0, imaginary=2.0)
print ComplexNumber(real=1.0, imaginary=0.0) * ComplexNumber(real=0.0, imaginary=1.0)
print ComplexNumber(real=10.0, imaginary=0.0) / ComplexNumber(real=-5.0, imaginary=0.0)
