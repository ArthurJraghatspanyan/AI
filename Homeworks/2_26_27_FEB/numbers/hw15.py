# Accept two fractions from the user and find their GCD using the math.gcd() function
# along with the numerator and denominator attributes of each fraction.

import math
import fractions

frac1 = fractions.Fraction(6, 9)
frac2 = fractions.Fraction(12, 27)

print(math.gcd(frac1.numerator, frac2.numerator))
print(math.gcd(frac1.denominator, frac2.denominator))