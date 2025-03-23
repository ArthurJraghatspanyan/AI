# Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.

import decimal

dec1 = decimal.Decimal('0.1')
dec2 = decimal.Decimal('0.2')
float1 = 0.1
float2 = 0.2

print(f"Summary of decimal is: {dec1 + dec2}\nSummary of float: {float1 + float2}")