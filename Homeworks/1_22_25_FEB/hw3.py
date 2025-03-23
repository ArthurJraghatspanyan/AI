# Create and Compare Numbers of Different Types
# Compare an integer and a float
# Compare a decimal and a float
# Compare two fractions

import decimal
import fractions

num_int = 5
num_float = 4.0

print(num_int > num_float)

num_dec = decimal.Decimal("5.0")

print(num_float < num_dec)

num_frac1 = fractions.Fraction(24, 5)
num_frac2 = fractions.Fraction(29, 4)

print(num_frac1 == num_frac2)