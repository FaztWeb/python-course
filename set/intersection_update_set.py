# keep only duplicate items in two sets
users1 = {"joe", "mark", "juan", "jane"}
users2 = {"maria", "marcus", "juan", "mark"}

users1.intersection_update(users2)

print(users1)
print(users2)
