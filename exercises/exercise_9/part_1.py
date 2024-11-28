class Complex:
    def __init__(self, re = 0, im = 0) -> None:
        self.re = re
        self.im = im
    
    # Addition
    def __add__(self, other):
        '''
        Only accepts "object + int/float"
        '''
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        else:
            return NotImplemented

    def __radd__(self, other):
        '''
        Handles cases when you write "int/float + object", which will throw "NotImplemented"
        '''
        return self.__add__(other)

    # Subract object with eithe object or int/float
    def __sub__(self, other):
        '''
        Only accepts "object - int/float"
        '''
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        else:
            return NotImplemented

    def __rsub__(self, other):
        '''
        Handles cases when you write "int/float - object", which will throw "NotImplemented"
        '''
        return self.__sub__(other)

    # Multiply object with eithe object or int/float
    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.re * other.re - self.im * other.im
            imag_part = self.re * other.im + self.im * other.re
        elif isinstance(other, (int,float)):
            return Complex(self.re * other, self.im * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # Check for 
    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        elif isinstance(other, (int, float)):
            return self.re == other and self.im == 0
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # Print conjugate
    def conjugate(self):
        return Complex(self.re, -self.im)
    

    def __str__(self):
        return f"{self.re} + {self.im}i"

    