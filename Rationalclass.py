class Rational:
    def __init__(self, a = 0, b = 1):
        if not isinstance(a,int) or not isinstance(b,int):
            raise TypeError('numerator and denominator must be integer')
        if b == 0:
            raise ValueError('denominator must not be 0')
        self.a = a
        self.b = b

        self._simplify()

    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        if self.a == 0:
            return '0'
        return  f'{self.a}/{self.b}'

    def _simplify(self):
        a = self.a
        b = self.b

        while b != 0:
            t = b
            b = a % b
            a = t
        self.a//= a
        self.b//= a

    def __add__(self, other):
        if isinstance(other,int):
            a = other*self.b + self.a
            b = self.b
        else:
            a = self.a*other.b + self.b * other.a
            b = self.b*self.b

        return Rational(a,b)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other,int):
            a = other*self.b - self.a
            b = self.b
        else:
            a = self.a*other.b - self.b * other.a
            b = self.b*self.b

        return Rational(a,b)

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, int):
            a = self.a * other
            b = self.b
        else:
            a = self.a * other.a
            b = self.b * other.b

        return Rational(a,b)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other,int):
            a = self.a
            b = self.b * other
        else:
            a = self.a * other.b
            b = self.b * other.a

        return  Rational(a,b)

    __rtruediv__ =  __truediv__




r = Rational(8,50)
print(r)
r2 = Rational(5,125)
print(r2)
result = r + r2
print(result)
result2 = r + 2
print(result2)
result3= 1 + r
print(result3)
result4 = r - r2
print(result4)
result5= 1 - r
print(result5)
