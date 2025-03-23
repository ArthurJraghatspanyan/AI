# Create two integer variables and perform addition, subtraction, multiplication, and division.
# Repeat the same for two floating-point numbers.
# Repeat the same for complex numbers.

num1_int = 12
num2_int = 6
num1_float = 12.5
num2_float = 6.5
num1_complex = 12 + 6j
num2_complex = 6 + 2j

add_int = num1_int + num2_int
sub_int = num1_int - num2_int
mul_int = num1_int * num2_int
div_true_int = num1_int // num2_int
div_floor_int = num1_int / num2_int

add_float = num1_float + num2_float
sub_float = num1_float - num2_float
mul_float = num1_float * num2_float
div_true_float = num1_float // num2_float
div_floor_float = num1_float / num2_float

add_complex = num1_complex + num2_complex
sub_complex = num1_complex - num2_complex
mul_complex = num1_complex * num2_complex
div_complex = num1_complex / num2_complex

print(f"Integers.\nAddition is: {add_int}\nSubtraction is: {sub_int}\nMultiplication is: {mul_int}\nTrue division is: {div_true_int}\nFloor division is: {div_floor_int}\n")
print(f"Float numbers.\nAddition is: {add_float}\nSubtraction is: {sub_float}\nMultiplication is: {mul_float}\nTrue division is: {div_true_float}\nFloor division is: {div_floor_float}\n")
print(f"Complex numbers.\nAddition is: {add_complex}\nSubtraction is: {sub_complex}\nMultiplication is: {mul_complex}\nDivision is: {div_complex}")