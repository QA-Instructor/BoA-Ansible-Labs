#! venv/bin/python3

users = {"learner" : "p@ssword", "student" : "secret"}

print(users)
valid_tokens = {user: [] for user in users.keys()}

print(valid_tokens)