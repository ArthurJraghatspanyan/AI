def max_length(sentence: str):
  ls = sentence.strip().split()
  max_length = ls[0]
  for i in range(1, len(ls)):
    if len(ls[i]) > len(max_length):
      max_length = ls[i]
  return max_length

print(max_length("Hello Python Welcome To PracticeWorkPython"))