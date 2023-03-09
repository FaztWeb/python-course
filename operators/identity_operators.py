names1 = ['John', 'Paul', 'George', 'Ringo']
names2 = ['John', 'Paul', 'George', 'Ringo']

print(names1 is names2) # False
print(names1 is not names2) # True

print(names1 == names2) # True
print(names1 != names2) # False

print("John" in names1) # True
print("John" not in names1) # False
