# Write a program that takes a string as input and outputs the longest substring without repeating characters.
# For example, the string "abcabcbb" should return "abc".

string = "abcdabcbbe"
new_st = ""
for i in range(len(string)):
  if string[i] not in new_st:
    new_st += string[i]
  else:
    break

print(new_st)