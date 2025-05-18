# Create a program that adds, subtracts, multiplies, and divides two integers, two floats, and a combination of both.

num1_int = 12
num2_int = 6
num1_float = 6.8
num2_float = 3.4

print(f"""Two integers.
      Addition: {num1_int + num2_int}
      Subtraction: {num1_int - num2_int}
      Multiplication: {num1_int * num2_int}
      True division: {num1_int // num2_int}
      Floor division: {num1_int / num2_int}""")

print(f"""Two floats.
      Addition: {num1_float + num2_float}
      Subtraction: {num1_float - num2_float}
      Multiplication: {num1_float * num2_float}
      True division: {num1_float // num2_float}
      Floor division: {num1_float / num2_float}""")

print(f"""Combination of both.
      Addition: {num1_int + num2_float}
      Subtraction: {num1_int - num2_float}
      Multiplication: {num1_int * num2_float}
      True division: {num1_int // num2_float}
      Floor division: {num1_int / num2_float}""")