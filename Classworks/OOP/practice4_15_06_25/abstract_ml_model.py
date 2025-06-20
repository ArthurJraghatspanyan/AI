# Simple Task: Abstract ML Model

import abc

class MLModel(abc.ABC):
  @abc.abstractmethod
  def train(self, data: list, labels: list):
    pass

  @abc.abstractmethod
  def predict(data: list):
    pass

class DummyClassifier(MLModel):
  frequency_data = {}
  def train(self, data: list, labels: list):
    if not isinstance(labels, list):
      raise TypeError("Type must be list...")
    if len(labels) <= 2:
      raise ValueError("Size of labels must be greater than 2...")
    if len(data) != len(labels):
      raise ValueError("Sizes of data and labels must be same...")
    for i in range(len(data)):
      if not isinstance(labels[i], int):
        raise TypeError("Labels must be integer type...")
      if not labels[i] in self.frequency_data.keys():
        self.frequency_data[labels[i]] = 1
      else:
        self.frequency_data[labels[i]] += 1

  def predict(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be list...")
    if len(data) <= 2:
      raise ValueError("Sizes of two data must be greater than 2...")
    res = []
    for _ in range(len(data)):
      start = 0
      for k, v in self.frequency_data.items():
        if v > start:
          start = v
          value = k
        else:
          continue
      res.append(value)

    return res

class AverageRegressor(MLModel):
  res = 0
  def train(self, data: list, labels: list):
    if not isinstance(labels, list):
      raise TypeError("Type must be list...")
    if len(data) != len(labels):
      raise ValueError("Sizes of data and labels must be same...")
    for i in range(len(data)):
      if not isinstance(labels[i], int):
        raise TypeError("Labels must be integer type...")
    self.res += sum(labels) / len(labels)

  def predict(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be list...")
    res = []
    for _ in range(len(data)):
      res.append(self.res)
    
    return res


clf = DummyClassifier()
clf.train([1, 2, 3, 4], [1, 1, 1, 1])
print(clf.predict([10, 20, 30, 40]))

print()

reg = AverageRegressor()
reg.train([1, 2, 3], [10, 20, 30])
print(reg.predict([4, 5]))