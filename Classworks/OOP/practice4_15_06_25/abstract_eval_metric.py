# Task: Abstract Evaluation Metric

import abc

class EvaluateMetric(abc.ABC):
  @abc.abstractmethod
  def calculate(self, y_true: list, y_pred: list):
    pass

class AccuracyMetric(EvaluateMetric):
  def calculate(self, y_true: list, y_pred: list):
    if not isinstance(y_true, list) or not isinstance(y_pred, list):
      raise TypeError("Type must be list...")
    if not y_true or not y_pred:
      raise ValueError("Lists must not be empty...")
    if len(y_true) != len(y_pred):
      raise ValueError("Size of two predictions must be same...")
    num_of_true = 0
    size = len(y_true)
    for i in range(size):
      if y_true[i] == y_pred[i]:
        num_of_true += 1
    accuracy = num_of_true / size
    return f"{accuracy} -> {num_of_true} correct out of {size}"

class MeanAbsoluteError(EvaluateMetric):
  def calculate(self, y_true: list, y_pred: list):
    if not isinstance(y_true, list) or not isinstance(y_pred, list):
      raise TypeError("Type must be list...")
    if not y_true or not y_pred:
      raise ValueError("Lists must not be empty...")
    if len(y_true) != len(y_pred):
      raise ValueError("Size of two predictions must be same...")
    n = len(y_true)
    summary = 0
    for i in range(n):
      summary += abs(y_true[i] - y_pred[i])
    res = summary / n
    return f"MAE is: {res:.2f}"
    

acc = AccuracyMetric()
print(acc.calculate([1, 0, 1, 1], [1, 0, 0, 1]))

mae = MeanAbsoluteError()
print(mae.calculate([10, 20, 30], [12, 18, 33]))