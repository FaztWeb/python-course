names = ("Joe", "Jane", "Jack", "Jill")
print(names)
print(type(names))

# convert to list
names_list = list(names)
print(names_list)
print(type(names_list))

# update values
names_list[0] = "Mike"
names_list[2] = "Mary"

# convert back to tuple
names = tuple(names_list)
print(names)
