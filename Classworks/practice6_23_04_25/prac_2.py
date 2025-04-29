# Assignment Instructions – Decorators in Python
# You need to create three custom decorators and use them together to enhance a function with useful behaviors like decoding input, encoding output,
# and logging the process.

import time
import base64

def decode(fn):
  def inner(*args, **kwargs):
    args = tuple(arg.decode('ascii') for arg in args)
    kwargs = {key : value.decode('ascii') for key, value in kwargs.items()}
    res = fn(*args, **kwargs)
    return res
  return inner

def encode(fn):
  def inner(*args, **kwargs):
    res = fn(*args, **kwargs)
    res = base64.b64encode(bytes(res, encoding='ascii'))
    return res
  return inner

def log(fn):
  def inner(*args, **kwargs):
    logger = open('log.txt', 'w')
    start = time.time()
    res = fn(*args, **kwargs)
    end = time.time()
    time_completed = end - start
    logger.write(f"Result in Base64 format: {res}" + "\n" + f"Time of function completed: {time_completed:.10f}s")
    return res
  return inner

@log
@encode
@decode
def greet(name):
  return f"Hello, {name}"

name_bytes = bytes("Arthur", encoding='ascii')

greet(name_bytes)