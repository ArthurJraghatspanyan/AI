# Write a program that checks whether a string starts with the letter "A" and ends with the letter "Z".
# # Input: "Amazing"
# # Output: Starts with A: True, Ends with Z: True

a_state = False
z_state = False

string = input("Enter your string: ")

if (ord(string[0]) == 65 or ord(string[0]) == 97) and (ord(string[-1]) == 90 or ord(string[-1]) == 122):
  a_state = True
  z_state = True
elif ord(string[0]) == 65 or ord(string[0]) == 97:
  a_state = True
elif ord(string[-1]) == 90 or ord(string[-1]) == 122:
  z_state = True

print(f"\nStarts with A, a: {a_state}, Ends with Z, z: {z_state}")