# Write a function register_user that accepts:
# A required positional argument: username.
# A required keyword-only argument: email.
# Hint: Use * to enforce keyword-only arguments.

def register_user(username, *, email="example@gmail.com"):
  return f"User with username: {username} and email: {email} registered successfully!"

print(register_user("arthur123", email="art.arm.2003@gmail.com"))