# Task 4: Model Evaluation with Default Values in __init__

import typing

class ModelEvaluator:
  def __init__(self, model_name: str, metrics: typing.List = ["accuracy"]):
    if not isinstance(model_name, str) or not isinstance(metrics, typing.List):
      raise TypeError("Invalid types for arguments. Model name must be string and metrics must be list.")
    self.model_name = model_name
    self.metrics = metrics
  def evaluate(self):
    for metric in self.metrics:
      print(f"Evaluating {self.model_name} using {metric}.")
  
modeval = ModelEvaluator("ImageClassifier")
modeval.evaluate()
modeval2 = ModelEvaluator("Normalization", ["accuracy", "length", "width"])
modeval2.evaluate()