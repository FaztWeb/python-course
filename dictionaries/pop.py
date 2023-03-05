# delete a key and return the value
user = {
    "name": "Jesus",
    "surname": "Fazt",
    "age": 20,
    "cities": ("Rio", "London", "San Francisco"),
    "active": True
}

print(user)

result = user.pop("cities")

print(user)
print("You removed the following cities", result)
