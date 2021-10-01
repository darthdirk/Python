import math
class Complex(object):
        def __init__(self, real, imaginary):
            self.real = real
            self.imaginary = imaginary
        def __add__(self, no):
                # (a+ib)+(c+id)=(a+c)+i(b+d)
            real = self.real + no.real
            imaginary = self.imaginary + no.imaginary
            return Complex(real, imaginary)
        def __sub__(self, no):
            # enter your code here
            # (a+ib)-(c+id)=(a-c)+i(b-d)
            real = self.real - no.real
            imaginary = self.imaginary - no.imaginary
            return Complex(real, imaginary)
        def __mul__(self, no):
            # enter code here
            # (a+ib)*(c+id)=(ac-bd)+i(ad+bc)
            real = (self.real*no.real - self.imaginary*no.imaginary)
            imaginary = (self.real*no.imaginary + self.imaginary*no.real)
            return Complex(real, imaginary)
        def __div__(self, no):
            # enter code here
            # (a+ib)/(c+id)=((ac+bd)+i(bc-ad))/(c^2+d^2)
            c_sqrd = no.real*no.real
            d_sqrd = no.imaginary*no.imaginary
            denominator = c_sqrd + d_sqrd
            real = (self.real*no.real + self.imaginary*no.imaginary) / (denominator)
            imaginary = (self.imaginary*no.real - self.real*no.imaginary) / (denominator)
            return Complex(real, imaginary)
        def mod(self):
            # enter your code here
            # mod of a+ib is equal to sq rt of a sq + b sq
            real = math.sqrt( self.real*self.real + self.imaginary*self.imaginary )
            #real = math.sqrt( ( self.real*self.real + self.imaginary*self.imaginary )
            return Complex(real, 0)
        def __str__(self):
            # enter code here
            real = "%.2f" % self.real
            imaginary = "%.2f" % self.imaginary
            if (self.imaginary) >= 0:
                    result = (str(real) + '+' + str(imaginary) + 'i' )
            else:
                result = (str(real) + '' + str(imaginary) + 'i' )
            return result
            # main method
        def main():
            if __name__ == '__main__':
                main()
C = map(float, input().split())
D = map(float, input().split())
x = Complex(*C)
y = Complex(*D)
print('\n'.join(map(str, [x.__add__(y), x.__sub__(y), x.__mul__(y), x.__div__(y), x.mod(), y.mod()]))
            #if __name__ == '__main__':
    #main()
