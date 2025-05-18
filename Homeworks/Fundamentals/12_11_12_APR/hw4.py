# Create a decorator require_login that only allows a function to execute if a global variable is_logged_in is True.
# If not, raise an exception.

def require_login(fn):
  def inner(*args, **kwargs):
    global is_logged_in
    if is_logged_in:
      res = fn(*args, **kwargs)
    return res
  return inner

@require_login 
def view_profile(): 
  print("Accessing user profile...")

# Toggle `is_logged_in` to test
is_logged_in = True
view_profile()
# Output:
# Accessing user profile...