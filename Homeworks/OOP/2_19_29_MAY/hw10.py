# Task 10: Encapsulation for AI Model Parameters

class AIModel:
  def __init__(self, learning_rate: int):
    if not isinstance(learning_rate, int):
      raise TypeError("Type must be int.")
    if learning_rate != 0 and learning_rate != 1:
      raise ValueError("Must be between 0 and 1")
    self.__learning_rate = learning_rate
  
  @property
  def learning_rate(self):
    return self.__learning_rate
  
  @learning_rate.setter
  def learning_rate(self, newLearningRate: int):
    if not isinstance(newLearningRate, int):
      raise TypeError("Type must be int.")
    if newLearningRate != 0 and newLearningRate != 1:
      raise ValueError("Must be between 0 and 1")
    self.__learning_rate = newLearningRate

ai = AIModel(1)
print(ai.learning_rate)
ai.learning_rate = -1   # ValueError: Must be between 0 and 1