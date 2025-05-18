# 3. Social Media Friend Suggestion (Dictionaries + Sets)
# Suggest friends for a user by finding friends of friends who are not already direct friends.

users_and_friends = {
  "Alice": {"Bob", "Charlie", "Eve"},
  "Bob": {"Charlie", "Alice", "Frank"},
  "Charlie": {"Alice", "Bob", "Hannah"},
}

all_users = set(users_and_friends.keys())
suggested_friends_of_friends = set()
others = set()

for user, friends in users_and_friends.items():
  friends_copy = friends.copy()
  if others:
    friends.update(others)
    others.clear()
  for friend in friends_copy:
    if friend in all_users:
      for suggest in users_and_friends[friend].copy():
        if suggest not in friends and suggest != user:
          friends.add(suggest)
    else:
      others.add(friend)
    friends.difference_update(friends_copy)

print(users_and_friends)