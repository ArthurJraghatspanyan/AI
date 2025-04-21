# Create a decorator require_login that only allows a function to execute if a global variable is_logged_in is True.
# If not, raise an exception.

def require_login(fn):
  def inner():
    global is_logged_in
    if is_logged_in:
      fn()
    return fn
  return inner

@require_login 
def view_profile(): 
  print("Accessing user profile...")

# Toggle `is_logged_in` to test
is_logged_in = False
view_profile()
# Output:
# Accessing user profile...