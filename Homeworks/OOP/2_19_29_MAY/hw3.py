# Task 3: AI Pipeline with Class Attributes and Instance Attributes

import typing

class AIPipeline:
  pipeline_count = 0
  def __init__(self, name: str, steps: typing.List):
    if not isinstance(name, str) or not isinstance(steps, typing.List):
      raise TypeError("Invalid types for arguments. Name must be string and steps must be list.")
    self.name = name
    self.steps = steps
    AIPipeline.pipeline_count += 1
  def __str__(self):
    return f"Pipeline name is: {self.name}\nSteps are: {self.steps}\nPipeline count: {self.pipeline_count}"
  
pipe1 = AIPipeline("HelperBot", ["cleaning", "training", "evaluation"])
print(pipe1)
pipe2 = AIPipeline("Synthia", ["teaching, making practices, doing lectures"])
print(pipe2)