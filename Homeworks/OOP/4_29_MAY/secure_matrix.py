# Task: Build a SecureMatrix Class (Encapsulation + 2D Data)

class SecureMatrix:
  def __init__(self, matrix: list, name: str):
    if not isinstance(matrix, list):
      raise TypeError("Type must be list...")
    if not matrix:
      raise ValueError("Matrix must not be empty...")
    for i in range(len(matrix)):
      if not isinstance(matrix[i], list):
        raise TypeError("Type of nested must be list...")
      if not matrix[i]:
        raise ValueError("List must not be empty...")
      if len(matrix[i]) != len(matrix[0]):
        raise ValueError("All rows must be at same length...")
    if not isinstance(name, str):
      raise TypeError("Type of name must be string...")
    if not name:
      raise ValueError("Name must not be empty...")

    self.__matrix = matrix
    self.__rows = len(matrix)
    self.__cols = len(matrix[0])
    self.__name = name

  @property
  def rows(self):
    return self.__rows
  
  @property
  def cols(self):
    return self.__cols
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, newName: str):
    if not isinstance(newName, str):
      raise TypeError("Type of name must be string...")
    if not newName:
      raise ValueError("Name must not be empty...")
    self.__name = newName

  def get(self, row: int, col: int):
    if not isinstance(row, int) or not isinstance(col, int):
      raise ValueError("Type of row and/or column must be integer...")
    if row + 1 > self.__rows:
      raise ValueError("Row is greater than actual rows matrix has...")
    if col + 1 > self.__cols:
      raise ValueError("Column is greater than actual rows matrix has...")
    return self.__matrix[row][col]
  
  def to_list(self):
    return self.__matrix.copy()
  
  def __repr__(self):
    return f"Matrix with name: {self.__name}.\nRows count is: {self.__rows}.\nColumns count is: {self.__cols}."


secmat = SecureMatrix([[1, 2, 4], [3, 4, 3]], 'SecuredArray')

print(secmat.cols)
print(secmat.rows)
print(secmat.name)
secmat.name = "SecuredMatrix"
print(secmat.name)

print(secmat.get(1, 2))
print(secmat.to_list())
print()
print(secmat)