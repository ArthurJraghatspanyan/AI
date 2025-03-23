# Accept two fractions from the user (in the form of a/b where both a and b are integers) and multiply them.
# Use the fractions.Fraction class to handle fractions and print the resulting fraction in its simplified form.

import fractions

a = int(input("Enter first numerator: "))
b = int(input("Enter first denominator: "))
c = int(input("Enter second numerator: "))
d = int(input("Enter second denominator: "))

frac1 = fractions.Fraction(a, b)
frac2 = fractions.Fraction(c, d)

mul = frac1 * frac2

print(f"Multiplication: {mul}")