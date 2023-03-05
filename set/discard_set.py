users = {"joe", "mark", "david", "marcus", "jane"}
print(users)

users.discard("joe")
print(users)

# remove an unknown item doesn not throw an error
users.discard("jim") 
