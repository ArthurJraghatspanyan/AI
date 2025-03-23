# Create Complex Numbers and Calculate Magnitude

# Create two fractions and perform addition, subtraction, multiplication, and division manually. Afterward, check the results using Python.

import fractions

num1 = fractions.Fraction(7, 13)
num2 = fractions.Fraction(8, 24)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"Addition is: {addition}")
print(f"Subtraction is: {subtraction}")
print(f"Multiplication is: {multiplication}")
print(f"Division is: {division}\n")

# Create a decimal number and experiment with adding or subtracting very small decimal values

import decimal

num = decimal.Decimal('3.14')
addition_dec = num + decimal.Decimal('0.00001')
subtraction_dec = num - decimal.Decimal('0.00000001')
print(f"Decimal addition is: {addition_dec}")
print(f"Decimal suntraction is: {subtraction_dec}")