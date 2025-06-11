# Task 1: Building a Simple AI Model Class

class AIModel:
  framework = "TensorFlow"
  def __init__(self, model_name: str, accuracy: float):
    if not isinstance(model_name, str) or not isinstance(accuracy, (int, float)):
      raise TypeError("Invalid types for arguments. Model name must be string, accuracy must be int or float.")
    if not 0 < accuracy <= 100:
      raise ValueError("Accuracy must be between 0 and 100.")
    self.model_name = model_name
    self.accuracy = float(accuracy)
  def display_info(self):
    return f"Model name is: {self.model_name}\nAccuracy is: {self.accuracy}\nFramework is: {self.framework}"

ai = AIModel("Image Classifier", 50)
print(ai.display_info())