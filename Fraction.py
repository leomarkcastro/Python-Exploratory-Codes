from math import *
from fractions import Fraction

print(Fraction(pi).limit_denominator(10))

ans = Fraction(10/7) + Fraction(2/3)

print(ans.limit_denominator(10))

