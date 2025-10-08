class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        divisor = Fraction.gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor

    #Getter
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    #Setter
    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            print("Incorrect logic: denominator cannot be zero")
            self._denominator = 1
        else:
            self._denominator = value

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"
    
    def __mul__(self, other):
        return Fraction(self._numerator * other._numerator, self._denominator * other._denominator)
    
    def __add__(self, other):
        n = (self._numerator * other._denominator) + (self._denominator * other._numerator)
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def __sub__(self, other):
        n = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def gcd(n, d):
        gcd = 1
        k = 1
        while k <= n and k <= d:
            if n % k == 0 and d % k == 0:
                gcd = k
            k += 1
        return gcd
    
frac1 = Fraction(2, 3)
print(frac1)

frac1.numerator = 3
frac1.denominator = 0
print(frac1)

frac2 = Fraction(4, 5)
print(f"{frac1} * {frac2} = {frac1 * frac2}")
print(frac1 + frac2)
print(frac1 -frac2)
