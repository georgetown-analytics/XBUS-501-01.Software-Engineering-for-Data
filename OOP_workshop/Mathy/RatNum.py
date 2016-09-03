class RationalNumber:
    """Any number that can be expressed as the quotient or fraction p/q
    of two integers, p and q, with the denominator q not equal to zero.

    Since q may be equal to 1, every integer is a rational number.

    Addition:        n1/d1 + n2/d2 = (n1*d2 + n2*d1)/(d1*d2)

    Subtraction:     n1/d1 - n2/d2 = (n1*d2 - n2*d1)/(d1*d2)

    Multiplication:  n1/d1 * n2/d2 = (n1*n2)/(d1*d2)

    Division:        (n1/d1) / (n2/d2) = (n1*d2)/(d1*n2)

    """

    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        '''Addition'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        '''Subtraction'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 - n2*d1, d1*d2)

    def __mul__(self, other):
        '''Multiplication'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*n2, d1*d2)

    def __truediv__(self, other):
        '''Division'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2, d1*n2)

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__

class Integer(RationalNumber):
    def __init__(self,number):
        self.n = number
        self.d = 1 #because the denominator will always be 1

if __name__ == "__main__":
    '''x = RationalNumber(1,2)
    y = RationalNumber(3,2)
    print ("The first number is {!s}".format(x))
    print ("The second number is {!s}".format(y))
    print ("Their sum is {!s}".format(x+y))
    print ("Their product is {!s}".format(x*y))
    print ("Their difference is {!s}".format(x-y))
    print ("Their quotient is {!s}".format(x/y))'''

    q = Integer(5)
    r = Integer(6)
    print ("{!s} is an integer expressed as a rational number".format(q))
    print ("So is {!s}".format(r))
    print ("When you add them you get {!s}".format(q+r))
    print ("When you multiply them you get {!s}".format(q*r))
    print ("When you subtract them you get {!s}".format(q-r))
    print ("When you divide them you get {!s}".format(q/r))
