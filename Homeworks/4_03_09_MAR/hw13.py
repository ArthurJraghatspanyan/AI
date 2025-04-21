# 1. Movie Recommendation System (Dictionaries + Sets)
# Given a dictionary of users and the movies they have watched, suggest movies that their friends have watched but they haven’t.

users_movies = {
  "Arthur": {"Inception", "The Grand Budapest Hotel", "Parasite"},
  "James": {"Parasite", "Spider-Man: Into the Spider-Verse", "Knives Out"},
  "Bob": {"Spider-Man: Into the Spider-Verse", "Knives Out", "The Shawshank Redemption"}
}

all_movies = set()
one_user_movies = set()

for movies in users_movies:
  all_movies.update(users_movies[movies])

for movies in users_movies:
  for suggest in all_movies:
    if suggest not in users_movies[movies]:
      one_user_movies.add(suggest)
  users_movies[movies].clear()
  users_movies[movies].update(one_user_movies)
  one_user_movies.clear()

print("Suggesting next movies for each user:\n")

for key, value in users_movies.items():
  print(key, ":", value)