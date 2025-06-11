# Task 2: Data Preprocessor Class with __str__ Method

class DataPreprocessor:
  def __init__(self, method: str, feature_count: int):
    if not isinstance(method, str) or not isinstance(feature_count, (int, float)):
      raise TypeError("Invalid types for class attributes.")
    if feature_count <= 0:
      raise ValueError("Feature count must be greater than 0.")
    self.method = method
    self.feature_count = feature_count
  def __str__(self):
    return f"Preprocessor using {self.method} on {self.feature_count} features."

datapreproc = DataPreprocessor("Normalization", 20)
print(datapreproc)