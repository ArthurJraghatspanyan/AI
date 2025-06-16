# Interface-Based File Parser System in Python

import csv
import json
from abc import ABC, abstractmethod

class IFileParser(ABC):
  @abstractmethod
  def parse(self, filepath: str):
    """
    Parse the given file and return its content.
    What to return depends on the file type:
    - CSV → list of dictionaries (one per row)
    - JSON → Python object (dict or list)
    - TXT → list of lines (strings)
    """
    pass

  @abstractmethod
  def file_type(self) -> str:
    """
    Return the file type handled by the parser (e.g., 'CSV', 'JSON', 'TXT').
    """
    pass

class CSVParser(IFileParser):
  def parse(self, filepath: str):
    if not isinstance(filepath, str):
      raise TypeError("Type of file must be string...")
    try:
      content = open(filepath)
      return list(csv.DictReader(content))
    except FileNotFoundError as e:
      raise e
  
  def file_type(self):
    return 'File type: CSV'

class JSONParser(IFileParser):
  def parse(self, filepath: str):
    if not isinstance(filepath, str):
      raise TypeError("Type of file must be string...")
    try:
      content = open(filepath)
      return json.load(content)
    except FileNotFoundError as e:
      raise e
  
  def file_type(self):
    return 'File type: JSON'

class TXTParser(IFileParser):
  def parse(self, filepath: str):
    if not isinstance(filepath, str):
      raise TypeError("Type of file must be string...")
    if not filepath.endswith('.txt'):
      raise ValueError("FIle must end with .csv...")
    try:
      content = open(filepath)
      ls = content.readlines()
      for i in range(len(ls)):
        if '\n' in ls[i]:
          ls[i] = ls[i].replace('\n', '')
      return ls
    except FileNotFoundError as e:
      raise e
  
  def file_type(self):
    return 'File type: TXT'

parser1 = CSVParser()
print(parser1.parse('username.csv'))
print(parser1.file_type())
print()
parser2 = JSONParser()
print(parser2.parse('students.json'))
print(parser2.file_type())
print()
parser3 = TXTParser()
print(parser3.parse('notes.txt'))
print(parser3.file_type())