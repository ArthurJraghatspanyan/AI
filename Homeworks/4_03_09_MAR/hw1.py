# Write a program that takes a sentence and creates a dictionary where each word is a key, and the value is the number of times that word appears.
# Use a sample sentence and break it into words to fill the dictionary. 
# Example: For the sentence "the cat and the hat", the dictionary should be {"the": 2, "cat": 1, "and": 1, "hat": 1}.

st = input("Enter your string: ")
di = {}
ls = st.strip().split()

for i in ls:
  if i not in di:
    di[i] = 1
  else:
    di[i] += 1

print(di)