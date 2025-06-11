# Task 5: AI Dataset Class with Both Class and Instance Attributes

class AIDataset:
  data_format = "CSV"
  def __init__(self, dataset_name: str, sample_count: int):
    if not isinstance(dataset_name, str) or not isinstance(sample_count, int):
      raise TypeError("Invalid types for arguments. Model name must be string and metrics must be list.")
    if sample_count <= 0:
      raise ValueError("Samples must be greater than 0.")
    self.dataset_name = dataset_name
    self.sample_count = sample_count
  def __str__(self):
    return f"Dataset: {self.dataset_name}, Samples: {self.sample_count}, Format: {self.data_format}"

dataset = AIDataset("Titanic", 891)
print(dataset)