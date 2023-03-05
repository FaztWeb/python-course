# keep all the items in two sets except the duplicates
users1 = {"joe", "mark", "juan", "jane"}
users2 = {"maria", "marcus", "juan", "mark"}

users1.symmetric_difference_update(users2)

print(users1)
