users1 = {"juan", "mark", "marcus", "martha" }
users2 = {"jane", "jim", "juan", "martha" }

print(users1)
print(users2)

res = users1.difference(users2)
res2 = users2.difference(users1)

print(res)
