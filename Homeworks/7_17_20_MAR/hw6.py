# Implement a function process_data that accepts a mix of positional arguments, default arguments,
# arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).
  # Require the first two arguments to be data (a list) and operation (a string that specifies the operation to perform:
  #   'sum', 'multiply', 'filter').
  # Optionally accept a trashhold parameter with a default value of None. This will only be used for the 'filter' operation.
  # Accept additional numbers via *args to be appended to the data list before processing.
  # Accept additional processing options through **kwargs, such as:
    # reverse (boolean): Whether to reverse the result.
    # unique (boolean): Whether to ensure the data list contains unique values before processing.
  # Function Behavior:
    # If the operation is 'sum', return the sum of the elements in the data list.
    # If the operation is 'multiply', return the product of the elements in the data list.
    # If the operation is 'filter', return a list of numbers greater than trashhold.
    # Apply reverse and unique options based on the kwargs values.

def process_data(it, operation, trashhold=None, *args, **kwargs):
  if not it:
    return "Data must not be empty"
  if not isinstance(it, list):
    return f"Data type of {it} must be list"
  for i in it:
    if not isinstance(i, int):
      return f"All data types of {it} must be int"
  if args:
    for i in args:
      if not isinstance(i, int):
        return "Data type must be int"
    it.extend(args)
  if kwargs.get("unique", False):
    it = list(set(it))
  if operation == 'sum':
    return sum(it)
  elif operation == 'multiply':
    multiply = 1
    for i in it:
      multiply *= i
      return multiply
  elif operation == 'filter':
    if trashhold == None:
      return it
    ls = []
    for i in it:
      if i > trashhold:
        ls.append(i)
    return list(reversed(ls)) if kwargs.get('reverse', False) else ls
  else:
    return f"There is not operation '{operation}'"

ls = [10, 20, 94]
print(process_data(ls, 'multiply'))
print(process_data(ls, 'filter'))
print(process_data(ls, 'filter', 6, reverse=True))
print(process_data(ls, 'sum'))